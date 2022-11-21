class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pardict = {
            ")":"(" ,
            "}":"{" ,
            "]":"[" 
        }
        for char in s:
            if char in "([{":
                stack.append(char)
            else:
                try:
                    stack[-1]
                except:
                    return False
                if pardict[char] == stack[-1]:
                    try:
                        stack.pop()
                    except:
                        return False
                else:
                    return False
        if stack == []:
            return True
        else:
            return False