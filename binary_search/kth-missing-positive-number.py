class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        if k<arr[0]:
            return k
        for i in arr:
            if k>=i:
                k+=1
        return k



class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        hash={}
        for i in arr:
            hash[i]=1
        missing=[]
        for i in range(1,max(arr)+k):
            if i not in hash:
                missing.append(i)
        if not missing:
            return max(arr)+k
        if len(missing)<k:
            while len(missing)!=k:
                missing.append(missing[-1]+1)
        return missing[k-1]