class Solution:
    def breakPalindrome(self, p: str) -> str:
        if len(p)==1:
            return ""
        p=list(p)
        if p.count('a')==len(p)-1 or p.count('a')==len(p):
            p[-1]='b'
        else:

            for ind,char in enumerate(p):
                if char!='a':
                    p[ind]='a'
                    break
        return ''.join(p)