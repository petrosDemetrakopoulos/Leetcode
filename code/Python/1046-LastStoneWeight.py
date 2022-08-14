class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        
        while len(stones) > 1:
            stones.sort(reverse=True)
            x = stones[1]
            y = stones[0]
            if x == y:
                stones = stones[2:]
            elif x != y:
                stones.pop(1)
                stones[0] = y-x
        if len(stones) > 0:
            return stones[0]
        return 0