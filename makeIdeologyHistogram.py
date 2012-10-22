
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.colors
import matplotlib.cm
import mpl_toolkits.axes_grid1.inset_locator as inset_locator
from mpl_toolkits.axes_grid1 import make_axes_locatable as make_axes_locatable

cNums = range(75,113)
#cNums = [111, 112]
print "Plotting Congresses:", str(cNums[0]), "-", str(cNums[-1])

#############################################
# get liberal-conservative dw-nominate scores
# taken from http://voteview.com/dwnominate.asp
import getNominateScores
import statecodes
d_scores = getNominateScores.getCongress(cNums, doPrint=False)
d_codesByState = statecodes.codesByState

congresses = []
polarizations = []
for cNum in cNums :
    
    print "...", str(cNum)
    
    fig = plt.figure(cNum, figsize=(10,8), dpi=100, edgecolor='white', facecolor='white')
    ax = fig.add_subplot(1,1,1)
    fig.subplots_adjust(bottom=0.08, top=0.95, left=0.1, right=0.95)
    ax.set_xlim(-1.0,1.0)
    ax.set_ylim(0.0, 5.5)
    xlabel = ax.set_xlabel("         < More Liberal -- More Conservative >", fontsize=18)
    ylabel = ax.set_ylabel("Density", fontsize=18, labelpad=15.0)
    ax.grid()
    #plt.setp(ax)

    diff = 111 - cNum
    yearLo = str(2008-(diff*2))
    yearHi = str(2010-(diff*2))
    if str(cNum).endswith("11") or str(cNum).endswith("12") or str(cNum).endswith("13") : numSuffix = "th"
    elif str(cNum).endswith("1") : numSuffix = "st"
    elif str(cNum).endswith("2") : numSuffix = "nd"
    elif str(cNum).endswith("3") : numSuffix = "rd"
    else : numSuffix = "th"
    tbox = ax.text(0.87, 0.91, str(cNum)+numSuffix+" Congress\n("+yearLo+"-"+yearHi+")", transform=ax.transAxes,
                fontsize=18, verticalalignment='center', horizontalalignment='center', multialignment='center',
                bbox=dict(boxstyle='round', facecolor='gold', linewidth=0.0, alpha=0.35))

    houseDems = []
    houseReps = []
    senateDems = []
    senateReps = []
    for district in d_scores :
        if not district.startswith(str(cNum)) : continue
        if d_scores[district]["nDistrict"] == 0 :
            if d_scores[district]["party"] == "Democrat" :
                senateDems.append(d_scores[district]["dim1"])
            if d_scores[district]["party"] == "Republican" :
                senateReps.append(d_scores[district]["dim1"])
        else :
            if d_scores[district]["party"] == "Democrat" :
                houseDems.append(d_scores[district]["dim1"])
            if d_scores[district]["party"] == "Republican" :
                houseReps.append(d_scores[district]["dim1"])
    
    demArr = np.asarray(houseDems+senateDems)
    repArr = np.asarray(houseReps+senateReps)
    demMean = np.mean(demArr)
    repMean = np.mean(repArr)

    bins = (-1.0,-0.9,-0.8,-0.7,-0.6,-0.5,-0.4,-0.3,-0.2,-0.1,0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0)
    
    nSD, binsSD, patchesSD = ax.hist(senateDems, bins=bins, normed=True, histtype='step', linewidth=3.0, linestyle='solid', color='blue', label='Senate Democrats')
    nSR, binsSR, patchesSR = ax.hist(senateReps, bins=bins, normed=True, histtype='step', linewidth=3.0, linestyle='solid', color='red', label='Senate Republicans')
    nHR, binsHR, patchesHR = ax.hist(houseReps, bins=bins, normed=True, histtype='step', linewidth=0.0, fill=True, alpha=0.5, facecolor='red', label='House Republicans')
    nHD, binsHD, patchesHD = ax.hist(houseDems, bins=bins, normed=True, histtype='step', linewidth=0.0, fill=True, alpha=0.5, facecolor='blue', label='House Democrats')

    legend = ax.legend(loc="upper left", ncol=1, fontsize=14, fancybox=True, frameon=False)
    legend.get_frame().set_alpha(0.5)
    
    demAnn = ax.annotate("Dems\nMean", horizontalalignment="center", fontsize=12, color='white',
                        xycoords='data', xy=(demMean,0.0), textcoords='data', xytext=(demMean,0.3),
                        arrowprops=dict(arrowstyle='simple', fill=True, facecolor='white', edgecolor='none'))
    repAnn = ax.annotate("Reps\nMean", horizontalalignment="center", fontsize=12, color='white',
                        xycoords='data', xy=(repMean,0.0), textcoords='data', xytext=(repMean,0.3),
                        arrowprops=dict(arrowstyle='simple', fill=True, facecolor='white', edgecolor='none'))

    ax_divider = make_axes_locatable(ax)
    ax_pol = ax_divider.append_axes("bottom", size="35%", pad=0.75)
    ax_pol.set_xlim(cNums[0], cNums[-1])
    ax_pol.set_xlabel("Congress", fontsize=18)
    ax_pol.set_ylabel("Polarization", fontsize=18, labelpad=15.0)
    congresses.append(cNum)
    polarizations.append(abs(demMean-repMean))
    ax_pol.plot(congresses, polarizations, color='purple', linewidth=2.0)
    ax_pol.plot(cNum, abs(demMean-repMean), color='purple', marker='o')
    
    plt.savefig("ideologyHists/"+str(cNum)+"hist.png")
    #plt.show()
    