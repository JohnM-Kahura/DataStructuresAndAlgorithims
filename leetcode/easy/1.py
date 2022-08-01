# my solution brute force
class Solution(object):
    def twoSum( nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i  in range(len(nums)):
            
            print(nums[i])
            for x in range(len(nums)):
                print(x)
                if nums[i]+nums[x] == target:
                    output=[i,x]
            # print(output)
        return output




