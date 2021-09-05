class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans=[0]
        max_profit, min_price = 0, float('inf')
        for price in prices:
            print(min_price)
            min_price = min(min_price, price)
            profit = price - min_price
            print('price',price)
            print('profit',profit)
            max_profit = max(max_profit, profit)
        return max_profit
        # for i in range(len(prices)):
        #     temp=[0]
        #     for j in range(i+1,len(prices)):
        #         if prices[j]-prices[i]>0:
        #             # print(temp)
        #             temp.append(prices[j]-prices[i])
        #     if max(temp)>ans[0]:
        #         ans.pop()
        #         ans.append(max(temp))
        #     temp=[0]
        # ans=0
        # buy=prices[0]
        # for i in range(len(prices)):
        #     ans=max(ans,prices[i]-buy)
        #     buy = min(prices[i],buy)
                # ans.pop()
                # ans.append(prices[i+1]-prices[i])
        
            
            # print('ans===>',ans)
        # return ans
        # buy = prices[0]
        # sell=0
        
#         if prices.index(buy)<prices.index(sell):
#             return sell-buy
#         else:
#             return 0
#         b=0
#         s=0
#         for i in range(1,len(prices)):
#             print('s{} and b{}'.format(s,b))
#             print('buy{} sell{}'.format(buy,sell))
#             # print(b)
#             # print(s)
#             if sell < prices[i] and i>b and sell>buy:
#                 sell=prices[i]
#                 s=i
#                 # print('buy')

#             elif buy > prices[i] :
#                 # print('sell')
#                 b=i
#                 buy = prices[i]
                
#         print(s)
#         print(b)
#         print(buy)
#         print(sell)
            
            
                
        