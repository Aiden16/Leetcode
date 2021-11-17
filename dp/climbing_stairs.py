class Solution:
    def climbStairs(self, n: int) -> int:
        dp=[0 for i in range(n+1)]
        dp[0]=1
        for i in range(1,n+1):
            if i==1:
                dp[i]=dp[i-1]
            else:
                dp[i]=dp[i-1]+dp[i-2]
        return dp[n]

        
        
# # Recursive function used by countWays
#         def countWaysUtil(n, m):
#             res = [0 for x in range(n)]
#             res[0], res[1] = 1, 1

#             for i in range(2, n):
#                 j = 1
#                 while j<= m and j<= i:
#                     res[i] = res[i] + res[i-j]
#                     j = j + 1
#             return res[n-1]

# # Returns number of ways to reach s'th stair
#         def countWays(s, m):
#             return countWaysUtil(s + 1, m)
	
#     # Driver Program
#         s, m = n, 2
#         return countWays(s,m)