class Solution(object):
    def findPeakElement(self, nums):
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            # If mid element is smaller than next element,
            # peak is on the right side.
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid

        return left
