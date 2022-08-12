class RecentCounter(object):
    
    def __init__(self):
        self.requests = []

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        if len(self.requests) > 0:
            if t > self.requests[len(self.requests) - 1] + 3000: #clear the requests array if no valid requests to reduce number of loops
                self.requests = []
        self.requests.append(t)
        res = []
        for i in self.requests:
            if i >= t-3000 and i <= t:
                res.append(i)
        return len(res)
                