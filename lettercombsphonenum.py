"""
Runtime: beats 99.57%
Memory: Beats 77.32%

A more simple method for this would be to utilize 
"""

import itertools
lstofdigits = ["22", "", "78", "2"]
letternum = {
    2 : 'abc',
    3 : 'def',
    4 : 'ghi',
    5 : 'jkl',
    6 : 'mno',
    7 : 'pqrs',
    8 : 'tuv',
    9 : 'wxyz'
}
def main(digits):
    if digits == "":
        return []
    def validity(comb):
        i = 0
        while i != len(digits):
            if comb[i] not in letternum[int(digits[i])]:
                return False
            i += 1
        return True
        
    def getletters(digits):
        letters = ""
        for i in range(len(digits)):
            if letternum[int(digits[i])] in letters:
                continue 
            letters += letternum[int(digits[i])]
        return letters
    lst = [''.join(x) for x in itertools.combinations(getletters(digits), len(digits)) if validity(x)]
    lst = [*set(lst)]
    return lst
for digits in lstofdigits:
    print(main(digits))