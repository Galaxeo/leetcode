class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        comp = ""
        num = 0
        c = 0
        print(len(s))
        for i in range(len(s)):
            if s[i] not in comp or s == " " or s == "":
                comp += s[i]
                c +=1
            else:
                split = comp.find(s[i])
                comp = comp[split+1:]
                comp += s[i]
                if c > num:
                    num = c
                c -= split
        if c > num:
            num = c
        return num