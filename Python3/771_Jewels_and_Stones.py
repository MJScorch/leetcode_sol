## Time: O(n*m)

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        def helper(jewels: str, stones: str, i: int, count: int):
            if i == len(jewels):
                return count
            else:
                return helper(jewels, stones, i+1, count + stones.count(jewels[i]))
    
        return helper(jewels, stones, 0, 0)
