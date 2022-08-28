class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        dest_cities = [paths[i][1] for i in xrange(len(paths))]
        outgoing_cities = [paths[i][0] for i in xrange(len(paths))]
        return[x for x in dest_cities if x not in outgoing_cities][0]