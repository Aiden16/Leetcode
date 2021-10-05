class Solution:
    def maxConsecutiveAnswers(self, a: str, k: int) -> int:
        #check for max true
        a=list(a)
        left=0
        T=k
        for right in range(len(a)):
            if a[right]=='F':
                T-=1
            if T<0:
                if a[left]=='F':
                    T+=1
                left+=1
        ansT=right-left+1
        left=0
        for right in range(len(a)):
            if a[right]=='T':
                k-=1
            if k<0:
                if a[left]=='T':
                    k+=1
                left+=1
        ansF=right-left+1
        # print(ansT,ansF)
        return max(ansT,ansF)
        