class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # pass
        # return [['a','a','b'],['b'],['aa']]
        self.arr=[]
        def recur(ques,ans):
            if ques=='':
                self.arr.append(ans)
                return 
            palin=''
            for i in range(len(ques)):
                palin=palin+ques[i]
                if palin==palin[::-1]:
                    recur(ques[i+1:],ans+[palin])

        recur(s,[])
        return self.arr