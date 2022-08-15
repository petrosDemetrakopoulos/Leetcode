class Solution(object):
    def findingUsersActiveMinutes(self, logs, k):
        """
        :type logs: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        hs = {}
        for log in logs:
            if log[0] not in hs:
                hs[log[0]] = {log[1]}
            else:
                hs[log[0]].add(log[1])
        for key in hs:
            hs[key] = len(hs[key])
        res = [0] * k
        for i in hs.values():
            res[i-1]+=1
        return res