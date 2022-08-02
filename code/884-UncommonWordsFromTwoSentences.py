class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        list1 = s1.split()
        list2 = s2.split()
        hash_tbl = {}
        res = [x for x in list1 if x not in list2] + [x for x in list2 if x not in list1]
        for i in res:
            if i not in hash_tbl:
                hash_tbl[i] = 1
            else:
                hash_tbl[i] += 1
        res = filter(lambda x: hash_tbl[x] == 1, res)
        return res