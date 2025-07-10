'''
with 3 angles, determine if the triangle is right, acute obtuse or invalid
a triangle is considered valid when all angles equal 180
the angles all must be greater then 0 as well
if angle1, angle2 and angle3 are all less then 90 then return acute
if max angle is greater then 90
return obtuse
if max angle is 90
return right angle
'''

def triangle(angle1, angle2, angle3):
    angle_list = [angle1, angle2, angle3]
    my_max = max(angle_list)
    my_sum = sum(angle_list)
    if my_sum != 180:
        return "invalid"
    
    if 0 in angle_list:
        return "invalid"
    
    if 90 in angle_list:
        return "right"
    if angle1 > 90 or angle2 > 90 or angle3 > 90:
        return "obtuse"
    
    return "acute"



print(triangle(60, 70, 50) == "acute")      # True
print(triangle(30, 90, 60) == "right")      # True
print(triangle(120, 50, 10) == "obtuse")    # True
print(triangle(0, 90, 90) == "invalid")     # True
print(triangle(50, 50, 50) == "invalid")    # True