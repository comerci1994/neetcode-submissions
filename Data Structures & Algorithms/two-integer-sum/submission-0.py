class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,num in enumerate(nums):
            rest_of_list = nums[i+1:]
            for j, other in enumerate(rest_of_list, start=i+1):
                if num + other == target:
                    return [i,j]