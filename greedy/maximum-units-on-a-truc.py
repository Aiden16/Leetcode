class Solution:
    def maximumUnits(self, b: List[List[int]], t: int) -> int:
        arr = sorted(b,key=lambda k:k[1],reverse=True)
        ans = 0
        for i in range(len(arr)):
            if t==0:
                break
            if arr[i][0]<t:
                ans += arr[i][0]*arr[i][1]
                t-=arr[i][0]
            else:
                ans+=t*arr[i][1]
                t-=t
        return ans