class Solution(object):
    def countGoodTriplets(self, arr, a, b, c):
        """
        :type arr: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        cnt = 0
        for i in xrange(len(arr)):
            for j in xrange(i,len(arr)):
                if j !=i:
                    for k in xrange(j,len(arr)):
                        if k!=j:
                            if abs(arr[i]-arr[j]) <= a and abs(arr[j]-arr[k]) <= b and abs(arr[i]-arr[k]) <= c:
                                cnt += 1
        return cnt