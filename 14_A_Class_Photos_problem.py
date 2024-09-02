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
