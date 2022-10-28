from csv_to_hashmap import get_map

# Create a hash table created from data in CVS file
current_hash = get_map()

# load truck 1 with packages that either must be delivered with other packages or have no start time constraints
truck1 = ['2', '7', '10', '13', '14', '15', '16', '19', '20', '27', '29', '30', '31', '34', '35', '39']
# Load truck 2 with packages that have start time or truck constraints, as well as other packages at the same address
truck2 = ['1' , '3' , '4' , '5', '6', '8', '12', '17', '18', '22', '25', '28', '32', '36', '37', '38']
# Load remaining packages on truck 3 (which is actually the second trip of truck 1)
truck3 = ['9', '11', '21', '23', '24', '26', '33', '40']

def run_route():

    
    return True # delete this. its's a place holder

def pkg_status(pkg, time):
    return True # delete this. its's a place holder

def route_mileage(route):
    return 140