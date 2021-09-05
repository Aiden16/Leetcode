class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        dic={}
        for i in arr:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        ans=sorted(list(set(arr)), key=lambda k : dic[k],reverse=True)
        count=0
        counter=0
        for i in ans:
            count+=dic[i]
            counter+=1
            if count>=len(arr)//2:
                return counter
        