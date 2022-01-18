class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #works
        dp=[float('Infinity') for i in range(amount+1)]
        # print(dp)
        dp[0]=0
        for i in range(len(coins)):
            for j in range(coins[i],len(dp)):
                dp[j]=min(dp[j-coins[i]]+1,dp[j])
        return dp[-1] if dp[-1]!=float('Infinity') else -1
        
        # generate all the possbile combinations but gave TLE 
        dp=[0 for i in range(amount+1)]
        dp[0]=1
        h=defaultdict(list)
        h[0].append('0')
        for i in range(len(coins)):
            # print(h)
            for j in range(coins[i],len(dp)):
                dp[j]+=dp[j-coins[i]]
                hash[dp[j]].append()
                for char in h[j-coins[i]]:
                    h[j].append(char+','+str(coins[i]))
        # print(h)
        # print(h[amount])
        am=None
        ans=float('Infinity')
        for i in h[amount]:
        #     # print(i)
            if ans>len(i):
                ans=len(i)
                am=i
        # # print(am)
        if not am:
            return -1
        am=len(am.split(','))
        # print(ans)
        # return ans-1
        return -1 if ans==float('Infinity') else am-1
            
        