'''
Two different python solutions here:

This first one is a very simple dictionary solution. By checking each 
character and the characters before it, it subtracts whenever it is needed 
then adds that number to the total sum.

The second solution uses string manipulation to change the strings where
subtraction is needed. Ex, 'IV' is changed to 'IIII'.
'''
# Solution 1 (Dictionary)
romandict= {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000}
s = 'MCMXCIV' 
sm = 0
i = 1
while i <= len(s):
    num = romandict[s[-i]]
    if i != len(s):
        if s[-i] in ('V', 'X'):
            if s[-i-1] == 'I':
                num -= 1
                i += 1
        elif s[-i] in ('L', 'C'):
            if s[-i-1] == 'X':
                num -= 10
                i += 1
        elif s[-i] in ('D', 'M'):
            if s[-i-1] == 'C':
                num -= 100
                i += 1
    sm += num
    i += 1
print(sm)

# Solution 2 (replace)
# I'm utilizing the same dictionary from solution 1 (romandict)

replacechar = {
        'IV' : 'IIII',
        'IX' : 'VIIII',
        "XL" : "XXXX",
        "XC" : "LXXXX",
        "CD" : "CCCC",
        "CM" : "DCCCC"
        }
sol2 = 0
for key, value in replacechar.items():
    s = s.replace(key, value)
for char in s:
    sol2 += romandict[char]
print(sol2)