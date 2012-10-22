
import politicalparty
d_party = politicalparty.d_party

import statecodes
d_codesByState = statecodes.codesByState

def getCongress(cNums, doPrint=True) :
    
    # http://voteview.com/dwnominate.asp
    #f = open('dwNominate.txt', 'r')
    f = open('commonSpaceDWNominate_1_111.txt', 'r')
    rawLines = f.readlines()
    d = {}
    
    for cNum in cNums :
        if doPrint is True :
            print "Congress =", cNum
        for rawLine in rawLines :
            line = rawLine.split()
            if int(line[0]) != int(cNum) : continue
            if len(line[2]) > 2 :
                line2 = line[2][:-2]
                line3 = line[2][-2:]
                line[2] = line2
                line.insert(3,line3)
            icpsr = line[2]
            nDistrict = line[3]
            #if int(nDistrict) == 0 : continue  # NO SENATE!
            state = statecodes.GetStateFromICPSR(int(icpsr))
            # unique congress+district identifier
            ID = str(cNum) + state + nDistrict
            try :
                d[ID]["nCongress"] = int(line[0])
            except KeyError :
                d[ID] = {}
                d[ID]["nCongress"] = int(line[0])
            d[ID]["icpsr"] = int(icpsr)
            d[ID]["nDistrict"] = int(nDistrict)
            if not line[5].isdigit() :
                line4 = str(line[4]+" "+line[5])
                line[4] = line4
                trash5 = line.pop(5)
            d[ID]["state"] = line[4]
            d[ID]["party"] = d_party[int(line[5])]
            while not line[7].replace(".","").replace("-","").isdigit() :
                line6 = str(line[6]+" "+line[7])
                line[6] = line6
                trash7 = line.pop(7)
            d[ID]["name"] = line[6]
            d[ID]["dim1"] = float(line[7])
            d[ID]["dim2"] = float(line[8])
            d[ID]["dim1StdErr"] = float(line[9])
            d[ID]["dim2StdErr"] = float(line[10])
        
            if doPrint is True :
                print ID
                print d[ID]["nDistrict"], d[ID]["state"], "("+str(d[ID]["icpsr"])+")"
                print "\t", d[ID]["party"], d[ID]["name"], "\t", d[ID]["dim1"], "+/-", d[ID]["dim1StdErr"], "\t", d[ID]["dim2"], "+/-", d[ID]["dim2StdErr"]
        
    return d
        
if __name__ == "__main__" :
    getCongress([112], True)
    
