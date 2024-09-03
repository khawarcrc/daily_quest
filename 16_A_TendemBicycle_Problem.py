# Problem Explanation
# Objective: Calculate the total speed of a tandem bicycle team based on the speeds of riders wearing red and blue shirts.

# Conditions:
# - Riders can be paired from the red and blue shirt groups.
# - You can either maximize the total speed or minimize it based on the fastest flag.

# Approach to Solve the Problem

# Step 1: Sort the Speeds
# - Sort the redShirtSpeeds and blueShirtSpeeds arrays in ascending order to align riders from slowest to fastest.

# Step 2: Adjust for Minimizing Speed (if applicable)
# - If fastest is False, reverse the redShirtSpeeds array to ensure the slowest red shirt riders pair with the fastest blue shirt riders to minimize the total speed.

# Step 3: Calculate Total Speed
# - Pair each red shirt rider with a blue shirt rider.
# - For each pair, choose the maximum speed of the two riders.
# - Sum these maximum speeds to get the total speed.


def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    # Sort both speed arrays in ascending order
    redShirtSpeeds.sort()
    blueShirtSpeeds.sort()

  
    print(f"Sorted red shirt speeds: {redShirtSpeeds}")
    print(f"Sorted blue shirt speeds: {blueShirtSpeeds}")

    # If we're not looking for the fastest possible outcome,
    # reverse the redShirtSpeeds array to pair the slowest red shirt rider
    # with the fastest blue shirt rider to minimize speed.
    if not fastest:
        reverseArrayInPlace(redShirtSpeeds)
        print(f"Reversed red shirt speeds for slowest total speed: {redShirtSpeeds}")

    totalSpeed = 0

    # Calculate total speed by selecting the maximum speed for each pair
    for idx in range(len(redShirtSpeeds)):
        rider1 = redShirtSpeeds[idx]
        rider2 = blueShirtSpeeds[len(blueShirtSpeeds) - idx - 1]  # Pairing the fastest available blue rider with red rider

        # Print current rider speeds for debugging
        print(f"Pair {idx + 1}: Red shirt rider speed = {rider1}, Blue shirt rider speed = {rider2}")
        
        totalSpeed += max(rider1, rider2)  # Add the maximum speed of the two riders in each pair

    # Print the total speed calculated
    print(f"Total speed: {totalSpeed}")
    
    return totalSpeed


def reverseArrayInPlace(array):
    # Reverses the given array in place
    start = 0
    end = len(array) - 1
    while start < end:
        array[start], array[end] = array[end], array[start]
        start += 1
        end -= 1


# Test the function with sample data
redShirtSpeeds = [5, 5, 3, 9, 2]
blueShirtSpeeds = [3, 6, 7, 2, 1]

# Example of fastest possible speed
print("Calculating fastest possible total speed:")
fastest = True
print(f"Maximum total speed: {tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest)}\n")

# Example of slowest possible speed
print("Calculating slowest possible total speed:")
fastest = False
print(f"Minimum total speed: {tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest)}")


# Time Complexity:
# The overall time complexity of the function is O(n log n) due to the sorting step,
# which dominates the O(n) time complexity of the pairing step.
