'''
there are 3600 minutes in an hour
play with this a little bit to see if we can find divisor by subtracting or adding


we can then convert the time into hours and minutes
format the string with padding if the number is less then 10

'''

def time_of_day(minutes):
    minutes_in_day = 24 * 60
    difference = minutes_in_day - minutes
    print(difference)
    print(difference / 60)




# print(time_of_day(0) == "00:00")        # True
# print(time_of_day(-3) == "23:57")       # True
# print(time_of_day(35) == "00:35")       # True
# print(time_of_day(-1437) == "00:03")    # True
# print(time_of_day(3000) == "02:00")     # True
# print(time_of_day(800) == "13:20")      # True
# print(time_of_day(-4231) == "01:29")    # True

time_of_day(3000)