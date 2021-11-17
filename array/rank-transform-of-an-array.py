class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        copied=arr.copy()
        copied.sort()
        rank=1
        h={}
        for i in copied:
            if i in h:
                continue
            h[i]=rank
            rank+=1
        ans=[]
        for i in arr:
            ans.append(h[i])
        return ans
        
        