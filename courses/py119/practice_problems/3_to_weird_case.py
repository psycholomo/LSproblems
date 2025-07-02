'''
Create a function that takes a string argument and returns a copy 
of the string with every second character in every third word 
converted to uppercase. Other characters should remain the same.

if the third word length is less then 2. just return the original letter
split the word into a list
for each word, if the word is the third, we can use modulo to see using a counter,
split the word into characters list
for every other character, replace the letter with an uppercase letter in the list
join the characters back together
replace the joined word in the list

join the list back together with white spaces

return the new constructed words

'''

def to_weird_case(word):
 
original = 'Lorem Ipsum is simply dummy text of the printing world'
expected = 'Lorem Ipsum iS simply dummy tExT of the pRiNtInG world'
print(to_weird_case(original) == expected)

original = 'It is a long established fact that a reader will be distracted'
expected = 'It is a long established fAcT that a rEaDeR will be dIsTrAcTeD'
print(to_weird_case(original) == expected)

print(to_weird_case('aaA bB c') == 'aaA bB c')

original = "Mary Poppins' favorite word is supercalifragilisticexpialidocious"
expected = "Mary Poppins' fAvOrItE word is sUpErCaLiFrAgIlIsTiCeXpIaLiDoCiOuS"
print(to_weird_case(original) == expected)