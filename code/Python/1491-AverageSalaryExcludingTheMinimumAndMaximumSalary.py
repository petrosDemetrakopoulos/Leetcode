class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        filtered = list(filter(lambda x: x != min(salary) and x != max(salary), salary))
        return float(sum(filtered)) / float(len(filtered))