class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans=[]
        for i in range(left,right+1):
            count=0
            arr=list(str(i))
            for num in arr:
                if int(num)==0:
                    count=0
                    break
                else:
                    if int(i)%int(num)==0:
                        count+=1
            if count==len(arr):
                ans.append(int(i))
        return ans