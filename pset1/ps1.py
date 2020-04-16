###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
"""
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
def greedy_cow_transport(cows,limit=10):
    trips = []
    cows_copy = cows.copy()
    sorted_cows = sorted(cows_copy.items(), key=lambda x: x[1], reverse=True)
    while sum(cows_copy.values()) > 0:
        ship = []
        rem_weight = limit
        for cow, weight in sorted_cows:
            if cows_copy[cow] > 0 and rem_weight >= weight:
                ship.append(cow)
                rem_weight -= weight
                cows_copy[cow] = 0
        trips.append(ship)
    return trips
            


# Problem 2
def brute_force_cow_transport(cows,limit=10):
    best_partition = None
    for partition in get_partitions(cows):
        all_ships_valid = True
        for ship in partition:
            ship_weight = 0
            for cow in ship:
                ship_weight += cows[cow]
            if ship_weight > limit:
                all_ships_valid = False
                break
        if not all_ships_valid:
            continue
        if best_partition == None or len(partition) < len(best_partition):
            best_partition = partition
    return best_partition

        
# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    cows = load_cows("ps1_cow_data.txt")
    start = time.time()
    print(greedy_cow_transport(cows))
    end = time.time()
    print(end - start)
    start = time.time()
    print(brute_force_cow_transport(cows))
    end = time.time()
    print(end - start)


"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

# cows = load_cows("ps1_cow_data.txt")
# limit=100
# print(cows)

# print(greedy_cow_transport(cows, limit))
# print(brute_force_cow_transport(cows, limit))
compare_cow_transport_algorithms()


