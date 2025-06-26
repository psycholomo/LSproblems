def xor(num1, num2):
    
    if num1 == True and num2 == True:
        return False
    elif num1 == False and num2 == False:
        return False
    else:
        return True
    



print(xor(5, 0) == True)
print(xor(False, True) == True)
print(xor(1, 1) == False)
print(xor(True, True) == False)

