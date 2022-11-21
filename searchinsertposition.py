class Solution(object):
    def binary_search(self, arr, low, high, x):
        if high >= low:
            mid = (high + low) // 2
            if x < arr[low]:
                return low
            if x> arr[high]:
                return high+1
            if arr[mid] == x:
                return mid
            elif arr[mid] > x:
                if arr[mid-1] < x:
                    return mid
                return self.binary_search(arr, low, mid - 1, x)
            else:
                if mid == high:
                    return high+1
                return self.binary_search(arr, mid + 1, high, x)
        else:
            return 
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(nums)-1
        mid = (low+high)//2
        return self.binary_search(nums, low, high, target)