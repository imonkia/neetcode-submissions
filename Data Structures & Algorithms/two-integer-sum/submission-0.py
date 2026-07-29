class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # 

        for i, val in enumerate(nums): # 
            complement = target - val # 7 - 3 = 4, 
            if complement in seen: # 4
                return [seen[complement], i]
            seen[val] = i
