# Problem Statement:
# You are given a circular route with `n` cities. Each city has a certain amount of fuel available,
# and it requires a certain distance to travel to the next city. Your vehicle can travel a specific
# number of miles per gallon (mpg). The task is to determine the first valid starting city where you 
# can complete the entire circular trip without running out of fuel. If no such city exists, return -1.

def validStartingCity(distance, fuel, mpg):
    # """
    # Determines the valid starting city for a circular trip where the car doesn't run out of fuel.
    # :param distance: List of distances between consecutive cities.
    # :param fuel: List of fuel available at each city.
    # :param mpg: Miles per gallon the vehicle can travel.
    # :return: Index of the valid starting city or -1 if none is valid.
    # """
    numberOfCities = len(distance)  # Total number of cities
    print(f"Total number of cities: {numberOfCities}")

    # Iterate through each city to check if it can be a valid starting city
    for startCityIdx in range(numberOfCities):
        milesRemaining = 0  # Start with 0 miles remaining
        print(f"\nChecking city index: {startCityIdx} as the starting point.")

        # Traverse the cities in a circular manner
        for currentCityIdx in range(startCityIdx, startCityIdx + numberOfCities):
            currentCityIdx = currentCityIdx % numberOfCities  # Handle circular traversal

            fuelFromCurrentCity = fuel[currentCityIdx]  # Fuel available at current city
            distanceToNextCity = distance[currentCityIdx]  # Distance to the next city
            # Calculate miles remaining after traveling to the next city
            milesRemaining += fuelFromCurrentCity * mpg - distanceToNextCity
            
            print(
                f"City {currentCityIdx}: Fuel = {fuelFromCurrentCity}, "
                f"Distance = {distanceToNextCity}, Miles Remaining = {milesRemaining}"
            )

            # If at any point milesRemaining is negative, this city cannot be a valid start
            if milesRemaining < 0:
                print(f"Cannot complete the trip starting at city {startCityIdx}.")
                break

        # If we complete the loop and milesRemaining is non-negative, this city is valid
        if milesRemaining >= 0:
            print(f"City {startCityIdx} is a valid starting point.")
            return startCityIdx

    print("No valid starting city found.")
    return -1  # If no valid starting city is found

# Dummy data
distance = [5, 25, 15, 10]  # Distances between cities
fuel = [4, 2, 1, 3]         # Fuel available at each city
mpg = 10                    # Miles per gallon

# Function call
starting_city = validStartingCity(distance, fuel, mpg)
print(f"\nValid starting city index: {starting_city}")
