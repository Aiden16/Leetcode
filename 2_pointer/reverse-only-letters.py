class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s=list(s)
        p1=0
        p2=len(s)-1
        while p1<=p2:
            if s[p1].isalpha() and s[p2].isalpha():
                s[p1],s[p2]=s[p2],s[p1]
                p1+=1
                p2-=1
            elif s[p1].isalpha():
                p2-=1
            elif s[p2].isalpha():
                p1+=1
            else:
                p1+=1
                p2-=1
        return ''.join(s)
            