class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        maxi = max(arr)
        for i in range(len(arr)):
            if arr[i] == maxi:
                return i
        