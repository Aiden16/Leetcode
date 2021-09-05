class Solution:
    def customSortString(self, order: str, s: str) -> str:
        new=''
        dic={}
        for i in s:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
        for i in order:
            if i in dic:
                new+=i*dic[i]
        for i in s:
            if i not in new:
                new+=i*dic[i]
        return new
         