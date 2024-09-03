# Problem Explanation
# Objective: Determine if it is possible to take a class photo such that all students wearing red shirts are in one row, 
# and all students wearing blue shirts are in another row. One row must be entirely shorter than the other.

# Conditions:
# - There are two rows of students: one row wears red shirts, and the other row wears blue shirts.
# - Each student in one row must be shorter than each student in the other row.
# - No two students from different rows can have the same height.

# Approach to Solve the Problem

# Step 1: Sort Heights
# - Sort both the redShirtsHeight and blueShirtsHeight arrays in descending order.
# - This allows us to compare the tallest student from each row down to the shortest.

# Step 2: Determine the First Row
# - Decide which group (red or blue) will be in the first row by comparing the tallest student of each group.
# - If the tallest red-shirted student is shorter than the tallest blue-shirted student, red shirts are in the front row, and vice versa.

# Step 3: Check the Height Condition
# - Iterate through both arrays and compare corresponding heights.
# - For the chosen front row (either red or blue), ensure every student in this row is shorter than the corresponding student in the back row.
# - If any student in the front row is not shorter than the corresponding student in the back row, return False.

# Step 4: Return Result


def classPhotos(redShirtsHeight, blueShirtsHeight):
    # Sort both lists in descending order
    redShirtsHeight.sort(reverse=True)
    blueShirtsHeight.sort(reverse=True)
    
    print("Sorted Red Shirts:", redShirtsHeight)
    print("Sorted Blue Shirts:", blueShirtsHeight)
    
    # Determine which shirt color will be in the first row
    shirtInFirstRow = 'Red' if redShirtsHeight[0] < blueShirtsHeight[0] else 'Blue'
    print("Shirts in First Row:", shirtInFirstRow)
    
    # Compare heights to ensure the correct row is taller
    for idx in range(len(redShirtsHeight)):
        redShirtHeight = redShirtsHeight[idx]
        blueShirtHeight = blueShirtsHeight[idx]
        
        print(f"Comparing heights: Red({redShirtHeight}) vs Blue({blueShirtHeight})")
        
        if shirtInFirstRow == 'Red':
            if redShirtHeight >= blueShirtHeight:
                print("Failed: Red shirt is not shorter")
                return False
        else:
            if blueShirtHeight >= redShirtHeight:
                print("Failed: Blue shirt is not shorter")
                return False
    
    print("Passed all checks")
    return True

redShirtsHeight = [5, 8, 1, 3, 4]
blueShirtsHeight = [6, 9, 2, 4, 5]

print(classPhotos(redShirtsHeight, blueShirtsHeight))  # Expected Output: True
