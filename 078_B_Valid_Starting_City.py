# Problem Statement:
# Given a list of distances between cities, a list of fuel available at each city,
# and the car's mileage (miles per gallon, mpg), determine the index of the city
# where a trip around all cities can start such that the car does not run out of fuel.
# The trip must start and end at the same city, visiting each city exactly once.

# Theory of Execution:
# 1. We calculate the net fuel miles remaining as we traverse from one city to the next.
# 2. If at any point, the fuel miles remaining are less than the lowest seen so far,
#    we update the potential starting city to the next city.
# 3. At the end of the traversal, the city with the lowest cumulative miles remaining
#    serves as the best starting point, as starting from there ensures we can complete
#    the circular journey without running out of fuel.

# Code with corrections, comments, and dummy data:


def validStartingCity(distances, fuel, mpg):
    """
    Determines the valid starting city for a circular trip.
    Parameters:
    - distances: List of distances between consecutive cities.
    - fuel: List of fuel available at each city.
    - mpg: Car mileage in miles per gallon.

    Returns:
    - Index of the starting city.
    """
    # Total number of cities
    numberOfCities = len(distances)

    # Tracks the current fuel miles remaining
    milesRemaining = 0

    # Tracks the index of the starting city candidate
    indexOfStartingCityCandidate = 0

    # Tracks the minimum miles remaining seen so far
    milesRemainingAtStartingCityCandidate = 0

    # Traverse through all cities
    for cityIdx in range(1, numberOfCities):
        # Calculate distance from the previous city
        distanceFromPreviousCity = distances[cityIdx - 1]

        # Calculate fuel gained at the previous city
        fuelFromPreviousCity = fuel[cityIdx - 1]

        # Update miles remaining by adding fuel and subtracting distance
        milesRemaining += fuelFromPreviousCity * mpg - distanceFromPreviousCity

        # If milesRemaining is less than the minimum so far, update starting city
        if milesRemaining < milesRemainingAtStartingCityCandidate:
            milesRemainingAtStartingCityCandidate = milesRemaining
            indexOfStartingCityCandidate = cityIdx

    # Return the index of the starting city candidate
    return indexOfStartingCityCandidate


# Dummy data for testing
distances = [5, 25, 15, 10, 20]  # Distances between consecutive cities
fuel = [1, 2, 1, 0.5, 3]  # Fuel available at each city
mpg = 10  # Miles per gallon of the car

# Expected output is the index of the valid starting city
print(validStartingCity(distances, fuel, mpg))  # Example output: 4



# Example Explanation:

# Input:
# - distances = [5, 25, 15, 10, 20]
# - fuel = [1, 2, 1, 0.5, 3]
# - mpg = 10

# Explanation:
# - At each city, calculate the fuel miles gained and subtract the distance to the next city.
# - The goal is to find a city where starting the journey ensures the car has enough fuel
#   to complete the circular trip without running out of fuel.

# Step-by-step:
# 1. Starting at city 0:
#    - Fuel gained = 1 gallon, miles from fuel = 1 * 10 = 10 miles.
#    - Distance to city 1 = 5 miles.
#    - Miles remaining after this leg = 10 - 5 = 5 miles.
#
# 2. Moving to city 1:
#    - Fuel gained = 2 gallons, miles from fuel = 2 * 10 = 20 miles.
#    - Distance to city 2 = 25 miles.
#    - Miles remaining after this leg = 5 + 20 - 25 = 0 miles.
#
# 3. Moving to city 2:
#    - Fuel gained = 1 gallon, miles from fuel = 1 * 10 = 10 miles.
#    - Distance to city 3 = 15 miles.
#    - Miles remaining after this leg = 0 + 10 - 15 = -5 miles.
#    - Since miles remaining is negative, the current starting point is not valid.
#    - Update the candidate starting city to city 3.
#
# 4. Moving to city 3:
#    - Fuel gained = 0.5 gallons, miles from fuel = 0.5 * 10 = 5 miles.
#    - Distance to city 4 = 10 miles.
#    - Miles remaining after this leg = -5 + 5 - 10 = -10 miles.
#    - Continue checking and update if necessary.
#
# 5. Moving to city 4:
#    - Fuel gained = 3 gallons, miles from fuel = 3 * 10 = 30 miles.
#    - Distance to city 0 = 20 miles.
#    - Miles remaining after this leg = -10 + 30 - 20 = 0 miles.
#
# Result:
# - The valid starting city is city 4 because it ensures the circular trip can be completed
#   without running out of fuel.
