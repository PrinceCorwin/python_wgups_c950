# Steve Amalfitano Student ID #: 010116956

# Import python datetime module
import datetime

# run_route is the central function of the program. It makes use of the Greedy Algorithm and finds the optimal delivery route for each truck using the nearest neigbor approach.
# Space-Time Complexity: O(n^2)
# It is this function that drives the Space-Time complexity of the entire program to be O(n^2)
from run_route import run_route

# Main function to initiate user interface functions
class Main: 
    # Call the run_route function to get delivery sequence and distance data
    del1, del2, del3, currentHash = run_route()

    # Function to lookup the delivery status of package selected by user at the time designated by user. Delivery times stored in the hashmap are converted to datetime objects for comparison to the user entered time of query
    #Space-Time complexity: O(1)
    def pkgStatus(pkg_id, time, hash):
        # check to see if it is time to change the address of package number 9
        if time.hour + time.minute / 60 + time.second / 3600 < 10.33:
            changeAddress = hash.get(('9'))
            changeAddress["Deliv Address"] = "300 State St"
            changeAddress["Zip"] = "84103"
        else:
            changeAddress = hash.get(('9'))
            changeAddress["Deliv Address"] = "410 S State St"
            changeAddress["Zip"] = "84111"
        currentPkg = hash.get(str(pkg_id))
        routeStart = datetime.timedelta(hours=float(currentPkg["Route Start"]))
        routeStart = datetime.datetime.strptime(str(routeStart), "%H:%M:%S")
        delivtime = datetime.timedelta(hours=float(currentPkg["Actual Deliv Time"]))
        delivtime = datetime.datetime.strptime(str(delivtime), "%H:%M:%S")
        if routeStart.time() > time.time():
            currentPkg["Delivery Status"] = f"At The Hub as of {time.time()}"
        elif delivtime.time() < time.time():
            currentPkg["Delivery Status"] = f"Delivered at {delivtime.time()}"
        else:
            currentPkg["Delivery Status"] = f"En Route as of {time.time()}" 
        # Lookup, return, and print the key-value attributes of the current package
        # Space-Time Complexity: O(1)
        PkgID = hash.lookup(str(pkg_id), "Pkg ID")
        address = hash.lookup(str(pkg_id), "Deliv Address")
        city = hash.lookup(str(pkg_id), "City")
        zip = hash.lookup(str(pkg_id), "Zip")
        weight = hash.lookup(str(pkg_id), "Weight")
        deadline = hash.lookup(str(pkg_id), "Delivery Deadline")
        status = hash.lookup(str(pkg_id), "Delivery Status")
        print(f"\nSTATUS OF PKG ID {PkgID} AT TIME {time.time()}")
        print("Route Start Time: ", routeStart.time())
        print("Delivery Address: ", address)
        print("Delivery City: ", city)
        print("Delivery Zip Code: ", zip)
        print("Delivery Weight: ", weight, "KILO")
        print("Delivery Deadline: ", deadline)
        print("Delivery Status: ", status)   
        print("Truck: ", currentPkg["Truck"])

    # Funtion to display total mileage for the three trucks at the specified time
    # Space-Time Complexity: O(1)
    def route_mileage(time, del1, del2, del3):
        # calculate miles unless query time is less than delivery start time
        # Space-Time Complexity: O(1)
        def get_miles(delivery, time):
            miles = 0
            hours = time.hour + time.minute / 60 + time.second / 3600
            if hours > delivery[3]:
                miles = min((hours - delivery[3]) * 18, delivery[1])
                miles = float("{:.2f}".format(min((hours - delivery[3]) * 18, delivery[1])))
                return miles
            return miles

        del1_miles = get_miles(del1, time)
        del2_miles = get_miles(del2, time)
        del3_miles = get_miles(del3, time)
        total_miles = float("{:.2f}".format(del1_miles + del2_miles + del3_miles))
        return del1_miles, del2_miles, del3_miles, total_miles


    # Interactive user interface printed to console when program runs
    # Glabal variables and User Instructions
    # Space-Time Complexity: O(1)
    num_pkgs = 40 # query this number  
    txt1 = "Step One:"
    txt2 = "Step Two:"
    print("\nWGUPS PACKAGE TRACKER")
    print("\nTo view the current delivery status for a given time:")
    print("{:<12}Enter time in HH:MM:SS format (24 hour military time).".format(txt1))
    print("{:<12}For midnight - 11 AM, HH = 00-11. Noon - 11 PM, HH = 12-23".format("", ""))
    print("{:<12}examples:".format(""))
    print("{:<12}9:02 and 23 seconds AM is 09:02:23".format(""))
    print("{:<12}2:17 and 45 seconds PM is 14:17:45".format(""))
    print("{:<12}Enter 'all' for all packages, or 'pkg' for specific package (user will be prompted for package ID).".format(txt2))
    print("\nEnter 'done' at any time to exit program.")

    # User interface begins with requesting and validating time from user
    # After time is determined by user, either a single package or all package statuses are printed to console
    # Space-Time Complexity: O(n)
    while True:
        mil_time_format = "%H:%M:%S"
        query_time = input("\nEnter time in HH:MM:SS format (or 'done' to exit): ").lower()
        if query_time == 'done':
            break
        try:
            valid_time = datetime.datetime.strptime(query_time, mil_time_format)

        # Upon invalid time entered, instuct user to enter correct format and continue loop
        except ValueError:
            print("HH, MM, and SS must be positive integers")
            print("HH must be 00-24")
            print("MM must be 00-60")
            print("SS must be 00-60")
            continue

        # Request and validate status from user of single or all packages
        while True:
            query_main = input("\nEnter 'all', 'pkg', or 'done' (no quotes): ").lower()
            if query_main != 'all' and query_main != 'pkg' and query_main != 'done':
                print("\nInvalid Entry")
                continue
            break
        if query_main == 'done':
            break
        elif query_main == 'pkg':

            # Request and validate package ID from user  
            # Space-Time Complexity: O(1)                  
            while True:
                pkg_id = input("Enter Package ID (or 'done' to exit): ").lower()
                if pkg_id == 'done':
                    break
                try:
                    pkg_id = int(pkg_id)

                # Upon invalid package id format, or id that doesn't exist entered, instuct user to enter correct format and continue loop
                except ValueError:
                    print("Package must be a positive integer")
                    continue
                if pkg_id >= 1 and pkg_id <= 40:
                    break
                else:
                    print(f'Current route has {num_pkgs} packages. Enter 1-{num_pkgs}')
            if pkg_id == 'done':
                break
            # print status of single package to console per ID selcted by user
            pkgStatus(pkg_id, valid_time, currentHash)
        else:
            # print status of all packages to console as requested by user. The pkgStatus function will be called for each package per truck that it is loaded on.
            # Space-Time Complexity: O(n)
            del1_miles, del2_miles, del3_miles, total_miles = route_mileage(valid_time, del1, del2, del3)
            print("\nALL PACKAGES ON DELIVERY 1 (TRUCK 1 FIRST TRIP):")
            for i in del1[2]:
                pkgStatus(i, valid_time, currentHash)
            print("\nALL PACKAGES ON DELIVERY 2 (TRUCK 2):")
            for i in del2[2]:
                pkgStatus(i, valid_time, currentHash)
            print("\nALL PACKAGES ON DELIVERY 3 (TRUCK 2 SECOND TRIP):")
            for i in del3[2]:
                pkgStatus(i, valid_time, currentHash)
            # Print mileage of each truck, as well as total mileage for all deliveries to the console
            print(f"\nTRUCK MILEAGE DATA AT TIME {valid_time.time()}:")
            print(f"First Delivery (Truck 1 first trip) mileage: {del1_miles} miles")
            print(f"Second Delivery (Truck 2): {del2_miles} miles")
            print(f"Third Delivery (Truck 1 second trip): {del3_miles} miles")
            print(f"Total Truck Mileage (all 3 Deliveries) at Time {valid_time.time()}: {total_miles} miles") 
        # Ask user if they want to continue with another query. Validate correct input format and either run the main while loop again, or break and end program
        # Space-Time complexity: O(1)
        while True:
            repeat = input("\nAnother Status Query? (y or n): ").lower()
            if repeat == 'y' or repeat == 'n' or repeat == 'done':
                break
            print("Invalid Entry")
            continue
        if repeat == 'done' or repeat == 'n':
            break
        continue
          
    

 