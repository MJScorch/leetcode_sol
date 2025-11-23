## Time: O(n**2)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for t in range(n-i-1):
                if (nums[i] + nums[t+i+1]) == target:
                    return [i,t+i+1]
