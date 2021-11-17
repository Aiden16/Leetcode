class Solution:
    def fib(self, n: int) -> int:
        #recur with memo
        qb=[0 for i in range(n+1)]
        def recurMemo(n,qb):
            if n==0 or n==1:
                return n
            if qb[n]!=0:
                return qb[n]
            f1=recurMemo(n-1,qb)
            f2=recurMemo(n-2,qb)
            fn=f1+f2
            qb[n]=fn
            return fn
        return recurMemo(n,qb)
        #recur 
        def fib(n):
            if n==1 or n==0:
                return n
            f1=fib(n-1)
            f2=fib(n-2)
            fn=f1+f2
            return fn
        return fib(n)
        # if n==0:
        #     return 0
        # f0=0
        # f1=1
        # fn=f0+f1
        # for i in range(n-1):
        #     fn=f0+f1
        #     f0=f1
        #     f1=fn
        # return fn       
        