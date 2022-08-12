class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        if len(trust) == 0:
            return n if n == 1 else -1
        hs = {}
        for i in trust:
            if i[0] not in hs:
                hs[i[0]] = [i[1]]
            else:
                hs[i[0]].append(i[1])
        all_persons = list(set(reduce(lambda x, y: x+ y, trust)))
        judge = [x for x in all_persons if x not in hs.keys()]

        if len(judge) > 1:
            return -1
        if len(judge) > 0:
            for i in hs:
                if judge[0] not in hs[i]:
                    return -1
            return judge[0]
        return -1