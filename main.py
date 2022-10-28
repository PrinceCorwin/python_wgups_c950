# Steve Amalfitano Student ID #: 010116956

# import csv
import datetime
from run_route import run_route, route_mileage, pkg_status

class Main:       
    # Interactive user interface printed to console when program runs
    # Glabal variables and User Instructions
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
            print(f"\nPackage {pkg_id} status at time {valid_time}")
            # pkgStatus(pkg_id, valid_time)
        else:
            print(f"\nStatus of all packages at time {valid_time}")
            # pkgStatus("all", valid_time)
        # Ask user if they want to continue with another query
        while True:
            repeat = input("Another Status Query? (y or n): ").lower()
            if repeat == 'y' or repeat == 'n' or repeat == 'done':
                break
            print("Invalid Entry")
            continue
        if repeat == 'done' or repeat == 'n':
            break
        continue
          
    

    