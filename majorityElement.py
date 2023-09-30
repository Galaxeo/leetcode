def majorityElement(lst):
    tempDict = {}
    for item in lst:
        if item not in tempDict:
            tempDict[item] = 1
        else:
            tempDict[item] += 1
            if tempDict[item] > len(lst)/2:
                return item
nums = [2,2,1,1,1,2,2]
print(majorityElement(nums))
