class Solution(object):
    def getKth(self, lo, hi, k):
        """
        :type lo: int
        :type hi: int
        :type k: int
        :rtype: int
        """
        arr = [[0,x] for x in range(lo,hi+1)]
        
        for i in xrange(len(arr)):
            pair = arr[i]
            crn_x = pair[1]
            steps = 0
            while crn_x != 1:
                if crn_x % 2 == 0:
                    crn_x = crn_x / 2
                else:
                    crn_x = 3 * crn_x + 1
                steps += 1
            pair[0] = steps
            arr[i] = pair
        sorted_arr = sorted(arr, key = lambda x: (x[0], x[1]))
        return sorted_arr[k-1][1]