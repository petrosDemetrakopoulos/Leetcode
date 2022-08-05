class Solution(object):
    def bestHand(self, ranks, suits):
        """
        :type ranks: List[int]
        :type suits: List[str]
        :rtype: str
        """
        if len(set(suits)) == 1:
            return 'Flush'
        ranks_dict = {}
        for i in ranks:
            if i not in ranks_dict:
                ranks_dict[i] = 1
            else:
                ranks_dict[i] += 1

        for rank in ranks_dict.values():
            if rank >= 3:
                return "Three of a Kind"
        for rank in ranks_dict.values():
            if rank == 2:
                return "Pair"
        return 'High Card'