import csv
from hashmap import HashMap

# Read CSV data into HashMap
# Space-time complexity: O(n)
with open('Python_WGUPS_C950\wgu_c950\PackagesForHash.csv') as csvfile:
    CSVData = csv.DictReader(csvfile, ("Pkg ID","Address", "City", "State", "Zip", "Deliv Time", "Mass", "Note"))
    # Create new empty instance of the HashMap class and Add each row of csv file to it
    PkgData = HashMap()
    PkgList = []
    for row in CSVData:
        row['Delivery Status'] = 'At Hub'
        PkgData.insert(row['Pkg ID'], row)
        PkgList.append(row['Pkg ID'])
    def get_map():
        return PkgData
    def get_pkg_list():
        return PkgList        
    
