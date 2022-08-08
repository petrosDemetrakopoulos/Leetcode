class MyHashSet(object):

    def __init__(self):
        self.hs = {}

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.hs[key] = ''
        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        if key in self.hs:
            del self.hs[key]
        

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        return key in self.hs


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)