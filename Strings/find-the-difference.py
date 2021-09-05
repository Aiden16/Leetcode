class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        hash={}
        for i in s:
            if i not in hash:
                hash[i]=1
            else:
                hash[i]+=1
        h={}
        for i in t:
            if i not in h:
                h[i]=1
            else:
                h[i]+=1
        for i in h.keys():
            if i in hash:
                if hash[i]!=h[i]:
                    return i
            else:
                return i
        