class Solution(object):
    def minMovesToSeat(self, seats, students):
        """
        :type seats: List[int]
        :type students: List[int]
        :rtype: int
        """
        seats.sort()
        students.sort()
        res = 0
        for i in xrange(len(seats)):
            res += abs(students[i] - seats[i])
        return res