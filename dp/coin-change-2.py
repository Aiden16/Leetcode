class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp=[0 for i in range(amount+1)]
        dp[0]=1
        for i in range(len(coins)):
            for j in range(coins[i],len(dp)):
                dp[j]+=dp[j-coins[i]]
        return dp[-1]