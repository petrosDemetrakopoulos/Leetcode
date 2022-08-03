class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        steps = 0
        reduced_num = num
        while reduced_num != 0:
            steps +=1
            if reduced_num % 2 == 0:
                reduced_num = reduced_num / 2
            else:
                reduced_num = reduced_num - 1
        return steps