'''
get a count for the length of the string.
if the letter is alpha
check if its lower or upper
if it is. throw it into the count for lower or upper
otherwise through it into the "nethier" bucket

Not sure on white spaces for this problem. ignore?

create a dictionary for upper count, lower count and neither
loop through each character and increment the count
testing shows that we do count white space as "neither

create a string formatter for the numbers that need to be represented
'''

def letter_percentages(words):
    letter_count = len(words)
    letter_dict_count = {"lowercase": 0,
                         "uppercase": 0,
                         "neither": 0}

    for letter in words:
        if letter.upper() == letter and letter.isalpha():

            letter_dict_count["uppercase"] += 1
        elif letter.lower() == letter and letter.isalpha():
            letter_dict_count["lowercase"] += 1
        else:
            letter_dict_count["neither"] += 1

    for key, value in letter_dict_count.items():
        letter_dict_count[key] = convert_num_to_percent_string(value, letter_count)
    print(letter_dict_count)
    return letter_dict_count
    

def convert_num_to_percent_string(num, total):
    total = (num / total) * 100
    return printy_print(total)



def printy_print(num):

    return (f'{float(num):.2f}')

expected_result = {
    'lowercase': "50.00",
    'uppercase': "10.00",
    'neither': "40.00",
}
print(letter_percentages('abCdef 123') == expected_result)

expected_result = {
    'lowercase': "37.50",
    'uppercase': "37.50",
    'neither': "25.00",
}
print(letter_percentages('AbCd +Ef') == expected_result)

expected_result = {
    'lowercase': "0.00",
    'uppercase': "0.00",
    'neither': "100.00",
}
print(letter_percentages('123') == expected_result)