class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        h1={}
        new=sorted(score,reverse=True)
        for ind,val in enumerate(new):
            h1[val]=ind
        ans=[]
        for i in range(len(score)):
            if h1[score[i]]+1==1:
                ans.append('Gold Medal')
            elif h1[score[i]]+1==2:
                ans.append('Silver Medal')
            elif h1[score[i]]+1==3:
                ans.append('Bronze Medal')
            else:
                ans.append(str(h1[score[i]]+1))
        return ans