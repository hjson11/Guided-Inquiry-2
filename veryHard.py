nums = [4,5,6,7,0,1,2]

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            return (nums.index(target))
        else:
            nums.append(target)
            nums.sort()
            return(nums.index(target))
