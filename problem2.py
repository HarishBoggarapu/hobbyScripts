
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(nums) - 1
        while(low <= high):
            mid = int((low + high) / 2)
            if (nums[mid] == target):
                return mid
            elif (nums[mid] <= nums[high]):
                if(target > nums[mid] and target <= nums[high]):
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                if (target >= nums[low] and target < nums[mid]):
                    high = mid - 1
                else:
                    low = mid + 1
        return -1


solution = Solution()
arr = [4, 5, 6, 7, 0, 1, 2]
print(solution.search(arr, 2))
