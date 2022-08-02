class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        flipped = map(lambda x: list(reversed(x)), image)
        for i in xrange(len(flipped)):
            for j in xrange(len(flipped[i])):
                if flipped[i][j] == 1:
                    flipped[i][j] = 0
                elif flipped[i][j] == 0:
                    flipped[i][j] = 1
                    
        return flipped