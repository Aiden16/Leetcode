class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        '''
        can take any digits
        need not to be consecutive
        '''
        if k>=len(num):
            return '0'
        stck = []
        vals = []
        #maintain monotonic increasing stack
        for i in range(len(num)):
            while stck and num[stck[-1]]>num[i] and k:
                stck.pop()
                vals.pop()
                k-=1
            stck.append(i)
            vals.append(num[i])
        i=0
        while k:
            vals.pop()
            k-=1
        c=0
        while i<len(vals) and vals[i]=='0':
            i+=1
            c+=1
        if not vals[c:]:
            return '0'
        return ''.join(vals[c:])