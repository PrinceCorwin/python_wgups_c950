import csv
from hashmap import HashMap

# Read CSV data into HashMap
# Space-time complexity: O(n)
with open('Python_WGUPS_C950\wgu_c950\PackagesForHash.csv') as csvfile:
    CSVPkgData = csv.DictReader(csvfile, ("Pkg ID","Deliv Address", "City", "State", "Zip", "Estimated Deliv Time", "Mass", "Note"))
    # Create new empty instance of the HashMap class and Add each row of csv file to it
    PkgData = HashMap()
    PkgList = []
    for row in CSVPkgData:
        row['Delivery Status'] = 'At Hub'
        row['Actual Deliv Time'] = ''
        PkgData.insert(row['Pkg ID'], row)
        PkgList.append(row['Pkg ID'])
    def get_map():
        return PkgData
    def get_pkg_list():
        return PkgList        
    
with open('Python_WGUPS_C950\wgu_c950\DistancesForHash.csv') as csvfile:
    CSVDistData = csv.DictReader(csvfile)
    DistData = {}
    for row in CSVDistData:
        DistData[row["Address"]] = row
    def get_dist_data():
        return DistData