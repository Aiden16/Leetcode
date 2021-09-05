class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        if k>len(s):
            return s[::-1]
        p1=0
        p2=k-1
        track=0
        s=list(s)
        while p2<len(s):
            track=p2+1
            while p1<=p2:
                s[p1],s[p2]=s[p2],s[p1]
                p1+=1
                p2-=1
            p1=track+k
            p2=p1+k-1
            if p2>len(s) or p2==len(s):
                p2=len(s)-1
                while p1<=p2:
                    s[p1],s[p2]=s[p2],s[p1]
                    p1+=1
                    p2-=1
                break
        return ''.join(s)
        pass
        