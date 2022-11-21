class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lst = ""
        num = 0
        mini = min(len(ele) for ele in strs)
        while num != mini:
            char = strs[0][num]
            for temp in range(len(strs)):
                if strs[temp][num] != char:
                    return lst
            lst+=strs[temp][num]
            num += 1
        return lst