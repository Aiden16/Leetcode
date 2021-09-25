class Solution:
    def tribonacci(self, n: int) -> int:
        f0=0
        f1=1
        f2=1
        fn=0
        if n==0:
            return 0
        if n<3:
            return 1 
        for i in range(n-2):
            fn=f1+f2+f0
            f0,f1,f2=f1,f2,fn
        return fn
        