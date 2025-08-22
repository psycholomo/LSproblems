def display_info(info,/,*,reverse=False,uppercase=False):
    if reverse==False and uppercase==False:
        return info
    elif reverse==True and uppercase == False:
        return info[::-1]
    elif reverse==False and uppercase == True:
        return info.upper()
    else:
        return info[::-1].upper()
                    
print(display_info("Launch", reverse=True)) # hcnuaL
print(display_info("School", uppercase=True)) # SCHOOL
print(display_info("cat", uppercase=True, reverse=True)) # TAC