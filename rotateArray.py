nums = [1,2,3,4,5,6,7]; k = 3 
def rotate(lst, k):
    k = k % len(lst)
    temp = lst[-k:] + lst[0:-k]
    counter = 0
    while counter != len(lst):
        lst[counter] = temp[counter]
        counter += 1
rotate(nums , 3)
print(nums)
