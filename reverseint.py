num = 123456789000
lst = []
#List manipulation
for dig in str(num):
    lst.append(dig)
#Set pointers
i = 0
j = len(lst)-1
#If the first char is a negative, we skip the first
if lst[0] == "-":
    i+=1
#We swap the first and the last, then increment/decrement the pointers
while i < j:
    lst[i], lst[j] = lst[j], lst[i]
    i+=1
    j-=1
#This removes the 0s from the beginning as we join the list
ret = int(''.join(map(str,lst)))
print(ret)