nums = [0,0,1,1,1,2,2,3,3,4]
# if doing first remove duplicates problem, modify such that
# the tempDict > 2 looks for tempDict > 1
# the solution is not optimized for the first problem but it does work
def removeDuplicates(lst):
    tempDict = {}
    i = 0;
    while i < len(lst):
        if lst[i] not in tempDict:
            tempDict[lst[i]] = 1
        else: 
            tempDict[lst[i]] += 1
            if tempDict[lst[i]] > 2:
                lst.remove(lst[i])
                continue
        i += 1
    return len(lst)
print(removeDuplicates(nums))
