class Solution(object):
    def groupThePeople(self, groupSizes):
        """
        :type groupSizes: List[int]
        :rtype: List[List[int]]
        """
        hm = {}
        res = []
        for key, val in enumerate(groupSizes):
            if val not in hm:
                hm[val] = [key]
            else:
                hm[val].append(key)

        for key in hm:
            arr_len = len(hm[key])
            while arr_len >= key:
                res.append(hm[key][:key])
                hm[key] = hm[key][key:]
                arr_len = len(hm[key])
        return res