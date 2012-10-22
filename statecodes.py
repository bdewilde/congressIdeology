
codesByState = {
    "USA": {"fips":99, "icpsr":99, "name":"UNITED STATES"},
    "AK" : {"fips":2, "icpsr":81, "name": "ALASKA"},
    "AL" : {"fips":1, "icpsr":41, "name": "ALABAMA"},
    "AR" : {"fips":5, "icpsr":42, "name": "ARKANSAS"},
    "AZ" : {"fips":4, "icpsr":61, "name": "ARIZONA"},
    "CA" : {"fips":6, "icpsr":71, "name": "CALIFORNIA"},
    "CO" : {"fips":8, "icpsr":62, "name": "COLORADO"},
    "CT" : {"fips":9, "icpsr":1, "name": "CONNECTICUT"},
    "DC" : {"fips":11, "icpsr":55, "name": "DISTRICT OF COLUMBIA"},
    "DE" : {"fips":10, "icpsr":11, "name": "DELAWARE"},
    "FL" : {"fips":12, "icpsr":43, "name": "FLORIDA"},
    "GA" : {"fips":13, "icpsr":44, "name": "GEORGIA"},
    "HI" : {"fips":15, "icpsr":82, "name": "HAWAII"},
    "IA" : {"fips":19, "icpsr":31, "name": "IOWA"},
    "ID" : {"fips":16, "icpsr":63, "name": "IDAHO"},
    "IL" : {"fips":17, "icpsr":21, "name": "ILLINOIS"},
    "IN" : {"fips":18, "icpsr":22, "name": "INDIANA"},
    "KS" : {"fips":20, "icpsr":32, "name": "KANSAS"},
    "KY" : {"fips":21, "icpsr":51, "name": "KENTUCKY"},
    "LA" : {"fips":22, "icpsr":45, "name": "LOUISIANA"},
    "MA" : {"fips":25, "icpsr":3, "name": "MASSACHUSETTS"},
    "MD" : {"fips":24, "icpsr":52, "name": "MARYLAND"},
    "ME" : {"fips":23, "icpsr":2, "name": "MAINE"},
    "MI" : {"fips":26, "icpsr":23, "name": "MICHIGAN"},
    "MN" : {"fips":27, "icpsr":33, "name": "MINNESOTA"},
    "MO" : {"fips":29, "icpsr":34, "name": "MISSOURI"},
    "MS" : {"fips":28, "icpsr":46, "name": "MISSISSIPPI"},
    "MT" : {"fips":30, "icpsr":64, "name": "MONTANA"},
    "NC" : {"fips":37, "icpsr":47, "name": "NORTH CAROLINA"},
    "ND" : {"fips":38, "icpsr":36, "name": "NORTH DAKOTA"},
    "NE" : {"fips":31, "icpsr":35, "name": "NEBRASKA"},
    "NH" : {"fips":33, "icpsr":4, "name": "NEW HAMPSHIRE"},
    "NJ" : {"fips":34, "icpsr":12, "name": "NEW JERSEY"},
    "NM" : {"fips":35, "icpsr":66, "name": "NEW MEXICO"},
    "NV" : {"fips":32, "icpsr":65, "name": "NEVADA"},
    "NY" : {"fips":36, "icpsr":13, "name": "NEW YORK"},
    "OH" : {"fips":39, "icpsr":24, "name": "OHIO"},
    "OK" : {"fips":40, "icpsr":53, "name": "OKLAHOMA"},
    "OR" : {"fips":41, "icpsr":72, "name": "OREGON"},
    "PA" : {"fips":42, "icpsr":14, "name": "PENNSYLVANIA"},
    "PR" : {"fips":72, "icpsr":0, "name": "PUERTO RICO"},
    "RI" : {"fips":44, "icpsr":5, "name": "RHODE ISLAND"},
    "SC" : {"fips":45, "icpsr":48, "name": "SOUTH CAROLINA"},
    "SD" : {"fips":46, "icpsr":37, "name": "SOUTH DAKOTA"},
    "TN" : {"fips":47, "icpsr":54, "name": "TENNESSEE"},
    "TX" : {"fips":48, "icpsr":49, "name": "TEXAS"},
    "UT" : {"fips":49, "icpsr":67, "name": "UTAH"},
    "VA" : {"fips":51, "icpsr":40, "name": "VIRGINIA"},
    "VT" : {"fips":50, "icpsr":6, "name": "VERMONT"},
    "WA" : {"fips":53, "icpsr":73, "name": "WASHINGTON"},
    "WI" : {"fips":55, "icpsr":25, "name": "WISCONSIN"},
    "WV" : {"fips":54, "icpsr":56, "name": "WEST VIRGINIA"},
    "WY" : {"fips":56, "icpsr":68, "name": "WYOMING"},
}

# returns two-letter state abbreviation given state's FIPS number
def GetStateFromFIPS(fips):
    
    for state in codesByState.keys() :
        for item in codesByState[state].items() :
            if item[0] == 'fips' and item[1] == fips :
                return state
    return -1


# returns two-letter state abbreviation given state's ICPSR number    
def GetStateFromICPSR(icpsr):
    
    for state in codesByState.keys() :
        for item in codesByState[state].items() :
            if item[0] == 'icpsr' and item[1] == icpsr :
                return state
    return -1


# executes when run from command line
if __name__ == "__main__" :
    
    print "put in code here"
    
    
    
    
    
    
    