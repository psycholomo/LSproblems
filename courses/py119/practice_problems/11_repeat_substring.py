'''
we need to find the smallest substring where the smallest substrings, length
multipled by each other will equal the length of the string.

if we slowly expand our substring, we can then check if it is divisble to the length of our main input
if it is divisible
we can check how many repetitions of that substring go into the string
by dividing the length of the original string with the length of the substring

if the substring multiplied by the repititions is the length of the string
return the tuple
'''

def repeated_substring(string):
    
    counter = 1
    
    while counter < len(string) + 1:
        substring = string[0:counter]
        if len(string) % len(substring) == 0:
            repetition = len(string) // len(substring)
            if repetition * substring == string:
                return (substring, repetition)
        counter += 1



        

print(repeated_substring('xyzxyzxyz') == ('xyz', 3))

print(repeated_substring('xyxy') == ('xy', 2))
print(repeated_substring('xyz') == ('xyz', 1))
print(repeated_substring('aaaaaaaa') == ('a', 8))
print(repeated_substring('superduper') == ('superduper', 1))