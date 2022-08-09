class Solution(object):
    def squareIsWhite(self, coordinates):
        """
        :type coordinates: str
        :rtype: bool
        """
        starts_with = True if int(coordinates[1]) % 2 == 0 else False
        for i in xrange(ord('a'),ord('h') + 1):
            if chr(i) != coordinates[0]:
                starts_with = not starts_with
            else:
                return starts_with