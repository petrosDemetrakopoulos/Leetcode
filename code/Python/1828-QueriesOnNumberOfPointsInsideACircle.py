class Solution(object):
    def countPoints(self, points, queries):
        """
        :type points: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        # x^2 + y^2 = r^2
        res = []
        for q in queries:
            cnt = 0
            qx = q[0]
            qy = q[1]
            qr = q[2]
            for point in points:
                x = point[0]
                y = point[1]
                circle = (x - qx)**2 + (y - qy)**2
                if (circle <= (qr)**2):
                    cnt += 1
            res.append(cnt)
        return res