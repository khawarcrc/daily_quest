# Problem Statement:
# Given a list 'seats' where each element is either a '1' (occupied seat) or '0' (empty seat),
# we need to find the index of the "best seat" that provides the maximum space between two occupied seats.
# The best seat is defined as the seat that is located in the middle of the longest segment of empty seats.

# Steps to Solve the Problem:

# 1. Initialize two variables:
#    - `bestSeat` to store the index of the best seat (set to -1 initially as no seat is found yet),
#    - `maxSpace` to track the maximum length of empty seat segments (set to 0 initially).

# 2. Start scanning the row of seats using a pointer `left` set to 0.
#    - The `left` pointer will represent the start of each segment of seats.

# 3. For each position of `left`, initialize another pointer `right` to `left + 1` to find the end of the segment of empty seats.
#    - Increment the `right` pointer until it encounters a taken seat (a `1`) or reaches the end of the list.
#    - This identifies a segment of consecutive empty seats (0s).

# 4. Calculate the size of the available space (number of empty seats) between the `left` and `right` pointers.
#    - This is done by subtracting `1` from `right - left` to exclude the seat occupied at the `left` position.

# 5. If this empty seat segment (available space) is larger than the previously recorded `maxSpace`:
#    - Update `bestSeat` to be the middle of the current segment (calculated as `(left + right) // 2`).
#    - Update `maxSpace` to the size of this segment.

# 6. Move the `left` pointer to the current `right` position to continue the search for the next segment of empty seats.

# 7. Repeat steps 3 to 6 until all seats have been scanned.

# 8. Finally, return the index of the best seat, or -1 if no empty seat exists.


def bestSeat(seats):
    # Initialize the variable to store the index of the best seat, -1 means no best seat found initially
    bestSeat = -1
    # Initialize maxSpace to 0, which keeps track of the largest segment of empty seats
    maxSpace = 0

    # Initialize left pointer to 0, which will scan the row from left to right
    left = 0

    # Loop through the seating arrangement
    while left < len(seats):
        # Initialize the right pointer to one seat ahead of the left pointer
        right = left + 1
        # Move the right pointer to the end of a segment of consecutive empty seats (0s)
        while right < len(seats) and seats[right] == 0:
            right += 1

        # Calculate the number of empty seats between two occupied seats (left and right pointers)
        availableSpace = right - left - 1

        # If the available empty space is larger than the previously recorded max space
        if availableSpace > maxSpace:
            # Update the bestSeat to be the middle seat in the current empty segment
            bestSeat = (left + right) // 2
            # Update the maxSpace to the size of the current segment
            maxSpace = availableSpace

        # Move the left pointer to the current right position to continue the search
        left = right

    # Return the index of the best seat found, or -1 if no empty seat exists
    return bestSeat


# Dummy data
seats = [1, 0, 0, 0, 1, 0, 0, 1]
print(
    "Best seat is at index:", bestSeat(seats)
)  # Output: 2 (middle of the longest empty segment [0, 0, 0])
