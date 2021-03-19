class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vals = {}
        for i,v in enumerate(nums):
            if (target - v) in vals:
                return [i , vals[(target - v)]]
            else:
                vals[v] = i        
