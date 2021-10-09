class MapSum(object):

    def __init__(self):
        self.d={}
        

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: None
        """
        self.d[key]=val

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        s=0
        for i in self.d.keys():
            if i[:len(prefix)]==prefix:
                s+=self.d[i]
        return s
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)