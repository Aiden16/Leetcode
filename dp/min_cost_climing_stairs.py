class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp=[0 for i in range(len(cost)+1)]
        for i in range(len(cost)-1,-1,-1):
            m=float('infinity')
            for j in range(1,3):
                if (i+j<len(dp)):
                    m=min(m,dp[i+j])
            dp[i]=m+cost[i]
        return min(dp[0],dp[1])


''''
java
'''

class Solution {
    public int minCostClimbingStairs(int[] cost) {
        
        int []dp = new int[cost.length+1];
        dp[0]=cost[0];
        dp[1]=cost[1];
        for(int i=2;i<cost.length;i++){
            dp[i]=Math.min(dp[i-1],dp[i-2])+cost[i];
        }
        return Math.min(dp[dp.length-2],dp[dp.length-3]);
    }
}




        