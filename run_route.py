from csv_to_hashmap import get_map, get_dist_data

# Create a hash table created from data in CVS file
current_hash = get_map()
DistData = get_dist_data()
# load truck 1 with packages that either must be delivered with other packages or have no start time constraints
truck1 = ['7', '10', '13', '14', '15', '16', '19', '20', '27', '29', '30', '31', '34', '35', '37', '39']

# Load truck 2 with packages that have start time or truck constraints, as well as other packages at the same address
truck2 = ['1', '2', '3', '4', '5', '6', '8', '12', '17', '18', '22', '25', '28', '32', '36', '38']

# Load remaining packages on truck 3 (which is actually the second trip of truck 1)
truck3 = ['9', '11', '21', '23', '24', '26', '33', '40']

# The main function to deliver the packages by calling the sub-function (truck_route) for each of the 3 trucks and return data
# Time-Space complexity: Initial function is O(1), but each of the sub functions called is O(n^2). Therefore, this function has a total complexity of O(n^2)
def run_route():
    truck1_start = 8
    truck1_list = truck_route(truck1, truck1_start, "Truck 1 (First Trip)")
    truck2_start = 9.08
    truck2_list = truck_route(truck2, truck2_start, "Truck 2")
    truck3_start = float("{:.2f}".format(truck1_start + (truck1_list[1] / 18)))
    truck3_list = truck_route(truck3, truck3_start, "Truck 1 (Second Trip)")
    return truck1_list, truck2_list, truck3_list, current_hash

# function to determine delivery sequence and distances for each truck. This uses the Greedy Neighbor algorithm
# Space-Time Complexity: O(n^2) due to while loop
def truck_route(truck, start, whichTruck):
    current_location = ["4001 South 700 East"]
    next_location = [""]
    current_pkg = [truck[0]]
    least_distance = 1000.00
    route = []
    delivered_pkg = []
    truck_distance = 0
    address_correction = False
    for i in truck:
        add_truck = current_hash.get(i)
        add_truck["Truck"] = whichTruck

    # Loop to determine which of the remaining packages to be delivered is closest to the previous delivery address. When found, that pkg will be appended to the route list. This will continue until all packages are delivered
    # Space-Time Complexity: O(n^2)
    while len(route) != len(truck):
        # check to see if Package 9 is on this truck and whether or not it is time to change the address
        if '9' in truck and start + (truck_distance / 18) > 10.33:
            newAddress = current_hash.get("9")
            newAddress["Deliv Address"] = "410 S State St"
            newAddress["Zip"] = "84111"
            address_correction = True
        for i in truck:
            if i not in delivered_pkg:
                # Conditional to verify that if package 9 is being considered for the next delivery, its addres has already been corrected. If it has not been corrected, it will not be considered
                if i != '9' or (i == '9' and address_correction == True):
                    data = current_hash.get(i)
                    next = data['Deliv Address']
                    miles = distance(current_location[0], next)
                    if miles < least_distance: # and miles != 0:
                        least_distance = miles
                        next_location[0] = next
                        current_pkg[0] = i

        # after for loop completes, The package with the closest proximity to the last delivery address will be appended to the route list. Distance and time will be added to their respective variables as well
        route.append(next_location[0])
        delivered_pkg.append(current_pkg[0])
        truck_distance += least_distance
        newDelivTime = current_hash.get(current_pkg[0])
        newDelivTime["Actual Deliv Time"] = start + (truck_distance / 18)
        newDelivTime["Route Start"] = start
        current_hash.insert(current_pkg[0], newDelivTime)
        # reset variable for next iteration of the while loop
        current_location = next_location
        next_location = [""]
        least_distance = 1000
    # add the distance for returning to hub to the total distance of the truck and return data values
    return_to_hub_dist = distance(route[-1], "4001 South 700 East")
    truck_distance += return_to_hub_dist
    truck_distance = float("{:.2f}".format(truck_distance))
    return [route, truck_distance, delivered_pkg, start]

# calculate distance between current package in the while loop above and the previous address.
# Space-Time Complexity: O(1)
def distance(current, next):
    if DistData[current][next] == '':
        miles = float(DistData[next][current])
    else:
        miles = float(DistData[current][next])
    return miles

