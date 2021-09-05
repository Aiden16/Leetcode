class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        ans=[]
        hash1={}
        for ind,val in enumerate(list1):
            hash1[val]=ind
        hash2={}
        counter=float('inf')
        for ind,val in enumerate(list2):
            if val in hash1:
                if counter>=ind+hash1[val]:
                    counter=min(counter,ind+hash1[val])
        for ind,val in enumerate(list2):
            if val in hash1:
                if ind+hash1[val]==counter:
                    ans.append(val)
        return ans
            