class BrowserHistory(object):

    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.backstack = []
        self.fwdstack = []
        self.curr = homepage

    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        self.backstack.append(self.curr)
        self.fwdstack = []
        self.curr = url
        

    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        if not self.backstack:
            return self.curr
        for i in xrange(steps):
            if self.backstack:
                poped = self.backstack.pop()
                self.fwdstack.append(self.curr)
                self.curr = poped
            else:
                return self.curr
        return self.curr

    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        if not self.fwdstack:
            return self.curr
        for i in xrange(steps):
            if self.fwdstack:
                poped = self.fwdstack.pop()
                self.backstack.append(self.curr)
                self.curr = poped
            else:
                return self.curr
        return self.curr
        

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)