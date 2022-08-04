class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        dest_cities = []
        outgoing_cities = []
        for i in xrange(len(paths)):
            outgoing_cities.append(paths[i][0])
            dest_cities.append(paths[i][1])
        return[x for x in dest_cities if x not in outgoing_cities][0]