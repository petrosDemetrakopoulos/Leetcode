class Solution(object):
    def mergeSimilarItems(self, items1, items2):
        """
        :type items1: List[List[int]]
        :type items2: List[List[int]]
        :rtype: List[List[int]]
        """
        hs = {}
        for item in items1:
            if item[0] not in hs:
                hs[item[0]] = item[1]
            else:
                hs[item[0]] += item[1]
        for item in items2:
            if item[0] not in hs:
                hs[item[0]] = item[1]
            else:
                hs[item[0]] += item[1]
        res = []
        for value in hs:
            res.append([value, hs[value]])
        res.sort(key= lambda x: x[0])
        return res