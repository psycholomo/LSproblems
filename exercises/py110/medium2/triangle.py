
'''
check to see if any of the angles are 0 or less.
 if so return "Invalid
 take the 3 inputs and make it a list so we can determine values more easily
 find the min
 find the max
 if all elements are the same return "equilateral
 if the two other numbers dont equal or greater then the  max
 return invalid

'''
def triangle(angle1,angle2,angle3):
    list_of_angles = [angle1, angle2, angle3]
    perimeter = sum(list_of_angles)
    if 0 in list_of_angles:
        
        return "invalid"
    if angle1 == angle2 == angle3:
        return "equilateral"
    
    minimum = min(list_of_angles)
    maximum = max(list_of_angles)
    middle = perimeter - maximum - minimum
    if minimum > 0 and minimum + middle > maximum:
        if angle1 == angle2 or angle1 == angle3 or angle2 == angle3:
            return "isosceles"
        else:
            return "scalene"
    return "invalid"



    
print(triangle(3, 3, 3) == "equilateral")  # True
print(triangle(3, 3, 1.5) == "isosceles")  # True
print(triangle(3, 4, 5) == "scalene")      # True
print(triangle(0, 3, 3) == "invalid")      # True
print(triangle(3, 1, 1) == "invalid")      # True