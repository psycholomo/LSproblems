from math import floor

DEGREE = f"\u00b0"

def create_str(num):
    if num < 10:
        return f"0{num}"
    else:
        return str(num)

def dms(my_float):
    degree = int(my_float)
    minutes = int((my_float - degree) * 60)
    seconds = int((my_float - degree - (minutes / 60)) * 3600)
    print(f"{create_str(degree)}{DEGREE}{create_str(minutes)}'{create_str(seconds)}\""
)
    return f"{degree}{DEGREE}{create_str(minutes)}'{create_str(seconds)}\""

print(dms(30) == "30°00'00\"")
print(dms(76.73) == "76°43'48\"")
print(dms(254.6) == "254°35'59\"" or dms(254.6) == "254°36'00\"")
print(dms(93.034773) == "93°02'05\"")
print(dms(0) == "0°00'00\"")
print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")