from __future__ import print_function
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon
import matplotlib.colors
import matplotlib.cm
import matplotlib.animation

cNums = [111]

#############################################
# get liberal-conservative dw-nominate scores
# taken from http://voteview.com/dwnominate.asp
import getNominateScores
import statecodes
d_scores = getNominateScores.getCongress(cNums, doPrint=False)
d_codesByState = statecodes.codesByState

#####################################
# set up figure, subplots, subaxes...
fig = plt.figure('map', figsize=(14,8), dpi=100, edgecolor='white', facecolor='white')
ax = fig.add_subplot(1,1,1)
fig.subplots_adjust(bottom=0.08, top=0.95, left=0.05, right=0.95)

import mpl_toolkits.axes_grid1.inset_locator as inset_locator
from mpl_toolkits.axes_grid1 import make_axes_locatable as make_axes_locatable

ax_divider = make_axes_locatable(ax)
ax_c = ax_divider.append_axes("bottom", size="10%", pad=0.1)

# set up a liberal-conservative color map
rgb = {
    'red':[(0.0, 0.0, 0.0), (0.5, 1.0, 1.0), (1.0, 1.0, 1.0)],
    'green':[(0.0, 0.0, 0.0), (0.5, 1.0, 1.0), (1.0, 0.0, 0.0)],
    'blue':[(0.0, 1.0, 1.0), (0.5, 1.0, 1.0), (1.0, 0.0, 0.0)]
    }
cmap_libcon = mpl.colors.LinearSegmentedColormap('lib-con', rgb)
norm = mpl.colors.Normalize(vmin=-1.0, vmax=1.0)
cb = mpl.colorbar.ColorbarBase(ax_c, cmap=cmap_libcon, norm=norm, orientation="horizontal")
cb.set_label("         < More Liberal -- More Conservative >", fontsize=16)

#################
# set up the maps
llclon = -128; llclat = 22; urclon = -64; urclat = 50

# draw canada and mexico
mCAN = Basemap(projection='mill', llcrnrlon=llclon, llcrnrlat=llclat, urcrnrlon=urclon, urcrnrlat=urclat,
            resolution='c', ax=ax)
shpCAN = mCAN.readshapefile("canada/canada", "canada", drawbounds=True, linewidth=0.5)
mMEX = Basemap(projection='mill', llcrnrlon=llclon, llcrnrlat=llclat, urcrnrlon=urclon, urcrnrlat=urclat,
            resolution='c', ax=ax)
shpMEX = mMEX.readshapefile("mexico/mexico", "mexico", drawbounds=True, linewidth=0.5)

ax_AK = inset_locator.inset_axes(ax, width="30%", height="30%", loc=3)
#ax_HI = inset_locator.inset_axes(ax, width="15%", height="15%", loc=3)

#axAK = fig.add_axes((0.03, 0.2, 0.2, 0.2))
#mAK = Basemap(projection='mill', llcrnrlon=-160, llcrnrlat=55, urcrnrlon=-140, urcrnrlat=65, resolution='h', ax=ax_inset)
#d_shpAKInfo = mAK.readshapefile("cd99_"+str(cNum)+"_shp/cd99_"+str(cNum), "districts", drawbounds=True)

mUSA = {}
mAK = {}
d_colors = {}
d_shpInfo = {}
d_shpAKInfo = {}
tbox = {}
for cNum in cNums :
    
    # Miller Cylindrical Projection map of lower 48 states
    mUSA[cNum] = Basemap(projection='mill', llcrnrlon=llclon, llcrnrlat=llclat, urcrnrlon=urclon, urcrnrlat=urclat,
                        resolution='h', ax=ax)
    # draw district boundaries
    # data from U.S Census Bureau, http://www.census.gov/geo/www/cob/cdXYZ.html
    d_shpInfo[cNum] = mUSA[cNum].readshapefile("cd99_"+str(cNum)+"_shp/cd99_"+str(cNum), "districts", drawbounds=False)
    mUSA[cNum].drawstates(linewidth=0.5)
    
    # Alaska inset
    mAK[cNum] = Basemap(projection='mill', llcrnrlon=-172, llcrnrlat=52, urcrnrlon=-129, urcrnrlat=72,
                        resolution='h', ax=ax_AK)
    d_shpAKInfo[cNum] = mAK[cNum].readshapefile("cd99_"+str(cNum)+"_shp/cd99_"+str(cNum), "districts", drawbounds=True)
    mAK[cNum].drawstates(linewidth=0.5)

    #print(cNum, ":", mUSA[cNum].districts_info[0].keys())
    for shapedict in mUSA[cNum].districts_info:
        i = mUSA[cNum].districts_info.index(shapedict)
        #print("\n", i, shapedict)
        nCD = shapedict["CD"]
        fips = shapedict["STATE"]
        state = statecodes.GetStateFromFIPS(int(fips))
        if state == "PR" or state == "DC" : continue     # no puerto rico or dc
        ID = str(cNum) + state + str(int(nCD))
        #if (d_scores[ID]["party"] == "Democrat" and d_scores[ID]["dim1"] > 0) or (d_scores[ID]["party"] == "Republican" and d_scores[ID]["dim1"] < 0):
        #    print(ID, d_scores[ID]["party"], d_scores[ID]["dim1"])
        #d_colors[mUSA[cNum].districts_info.index(shapedict)] = cmap_libcon(d_scores[ID]["dim1"])
        if str(cNum)+state+"2" in d_scores :
            if nCD == 0 : continue
        else : ID = str(cNum) + state + str(1)
        #print(ID)
        seg = mUSA[cNum].districts[i]
        color = cmap_libcon(d_scores[ID]["dim1"])
        poly = Polygon(seg, facecolor=color, edgecolor=color)
        ax.add_patch(poly)

    """
    # cycle through names, color each one
    for nshape,seg in enumerate(mUSA[cNum].districts):
        print(nshape,seg)
        state = statecodes.GetStateFromFIPS(int(mUSA[cNum].districts_info[nshape]["STATE"]))
        if int(mUSA[cNum].districts_info[nshape]["CD"]) == 0 : continue    # SENATE
        if state == "PR" or state == "DC" : continue
        color = d_colors[nshape]
        poly = Polygon(seg, facecolor=color, edgecolor=color, )
        ax.add_patch(poly)
    """
    """
    # do the same for alaska
    for shapedict in mAK[cNum].districts_info :
        nCD = shapedict["CD"]
        fips = shapedict["STATE"]
        state = statecodes.GetStateFromFIPS(int(fips))
        if state != "AK" : continue
        ID = str(cNum) + state + str(int(nCD))
        #print(ID, d_scores[ID])
        d_colors[mAK[cNum].districts_info.index(shapedict)] = cmap_libcon(d_scores[ID]["dim1"])
        
    # cycle through names, color each one
    for nshape,seg in enumerate(mAK[cNum].districts) :
        state = statecodes.GetStateFromFIPS(int(mAK[cNum].districts_info[nshape]["STATE"]))
        if state != "AK" : continue
        color = d_colors[nshape]
        poly = Polygon(seg, facecolor=color, edgecolor=color, )
        ax_AK.add_patch(poly)
    """
    # text box showing which congress
    diff = 111 - cNum
    yearLo = str(2008-(diff*2))
    yearHi = str(2010-(diff*2))
    tbox[cNum] = ax.text(0.88, 0.2, str(cNum)+"th House\n("+yearLo+"-"+yearHi+")", transform=ax.transAxes,
                fontsize=22, verticalalignment='center', horizontalalignment='center', multialignment='center',
                bbox=dict(boxstyle='round', facecolor='gold', linewidth=0.0, alpha=0.35))

    #plt.tight_layout()
    plt.show()
    #plt.savefig(str(cNum)+".png")
    tbox[cNum].remove()

