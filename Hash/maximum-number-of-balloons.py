class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        fre={}
        s='balloon'
        for i in text:
            if i in fre:
                fre[i]+=1
            elif i in s:
                fre[i]=1
        c=0
        if 'l' in fre and 'o' in fre:
            fre['l']//=2
            fre['o']//=2
        if len(fre)==5 and fre['l']>=1 and fre['o']>=1:
            m=fre['b']
            for i in s:
                m=min(m,fre[i])
            return m
        return 0
