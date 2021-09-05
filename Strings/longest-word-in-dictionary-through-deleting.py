class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        def check(c,s):
            p1=0
            p2=0
            stack=[]
            while p1!=len(c) and p2!=len(s):
                if s[p2]==c[p1]:
                    stack.append(s[p2])
                    p2+=1
                    p1+=1
                else:
                    p2+=1
            return ''.join(stack)==c
        ans=[]
        for i in d:
            if check(i,s):
                ans.append(i)
        if not ans:
            return ''
        ans.sort(key=lambda k : len(k),reverse=True)
        ac=[]
        for i in ans:
            if len(i)==len(ans[0]):
                ac.append(i)
        ac.sort()
        return ac[0]


class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        def check(c,s):
            p1=0
            p2=0
            stack=[]
            while p1!=len(c) and p2!=len(s):
                if s[p2]==c[p1]:
                    stack.append(s[p2])
                    p2+=1
                    p1+=1
                else:
                    p2+=1
            return len(stack)==len(c)
        subq=''
        subl=0
        for i in d:
            if check(i,s):
                if len(i)>subl:
                    subq=i
                    subl=len(subq)
                elif len(i)==subl:
                    subq=min(i,subq)
        return subq

        