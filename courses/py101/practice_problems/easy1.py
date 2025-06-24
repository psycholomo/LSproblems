#1 yes because 6 is out of bounds

# #2
# str1 = "Come over here!"  # True
# str2 = "What's up, Doc?"  # False

# def end_exclamation(input_string):
#     if  input_string[-1] == "!":
#         return True
    
#     return False


# print(end_exclamation(str1))

#3

# famous_words = "seven years ago. . ."

# appending = "Four score and "

# new_string = famous_words + appending

# new_string = f"{appending} {famous_words}"

#4

# munsters_description = "the Munsters are CREEPY and Spooky."
# print(munsters_description.lower())

#5
# munsters_description = "The Munsters are creepy and spooky."
# print(munsters_description.swapcase())

#6
# str1 = "Few things in life are as important as house training your pet dinosaur."
# str2 = "Fred and Wilma have a pet dinosaur named Dino."

# if str2.find("Dino") >= 0:
#     print(True)
# else:
#     print(False)
# print(str1.find("Dino"))
# print(str2.find("Dino"))
# #shorthands
# 'Dino' in str1
# 'Dino' in str2

# #7
# flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]
# flintstones.append("Dino")
# newArr = flintstones + ['Dino']

#8 to add multiple values
# flinstones.extend(['Dino','Hoppy'])
#9
# advice = "Few things in life are as important as house training your pet dinosaur."
# sliced_advice = advice[0:45]
# print(sliced_advice)
# advice.split("house")[0]
# print(advice)

#10
advice = "Few things in life are as important as house training your pet dinosaur."

advice = advice.replace("important", "urgent")
print(advice)