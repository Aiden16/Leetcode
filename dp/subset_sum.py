class Solution:
    def isSubsetSum (self, N, arr, sum):
        # code here 
        
        dp=[]
        for i in range(len(arr)+1):
            tmp=[]
            for j in range(sum+1):
                tmp.append(0)
            dp.append(tmp)
        # print(dp)
        for i in range(len(arr)+1):
            for j in range(sum+1):
                #first cell
                if i==0 and j==0:
                    dp[i][j]=True
                #first row
                elif i==0:
                    dp[i][j]=False
                #first column
                elif j==0:
                    dp[i][j]=True
                #rest of the cells
                else:
                    #above the row
                    if dp[i-1][j]:
                        dp[i][j]=True
                    else:
                        val = arr[i-1]
                        if j>=val:
                            if dp[i-1][j-val]:
                                dp[i][j]=True
        # print(dp)
        return 1 if dp[len(arr)][sum] else 0