class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        h1={}
        h2={}
        if len(s1)>len(s2):
            return False
        for i in s1:
            h1[i]=h1.get(i,0)+1
        for i in range(len(s1)):
            h2[s2[i]]=h2.get(s2[i],0)+1
        if h1==h2:
            return True
        for i in range(len(s1),len(s2)):
            left=i-len(s1)
            if h2[s2[left]]==1:
                del h2[s2[left]]
            else:
                h2[s2[left]]-=1
            h2[s2[i]]=h2.get(s2[i],0)+1
            if h2==h1:
                return True
        return False