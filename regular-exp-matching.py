s = "aa"
p = "a"


def check(s, p):
    for i in range(len(s)):
        if s[i] == p[i]:
            continue
        else:
            
    return True

def main():
    #Basic check
    if len(s) != len(p):
        return False
    elif s == p:
        return True 
    for i in range(len(s)):
