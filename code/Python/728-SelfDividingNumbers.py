class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        res = []
        for i in range(left,right+1):
            str_num = str(i)
            digits = list(map(lambda x: int(x), list(str_num)))
            is_self_dividing = True
            for j in digits:
                if j != 0:
                    if i % j != 0:
                        is_self_dividing = False
                else:
                    is_self_dividing = False
            if is_self_dividing:
                res.append(i)
        return res