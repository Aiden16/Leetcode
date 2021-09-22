class Solution:
    def maxLength(self, arr: List[str]) -> int:
        ans=0
        res=['']
        for i in range(len(arr)):
            # print(res)
            for j in range(len(res)):
                s=arr[i]+res[j]
                if len(set(s))==len(s):
                    res.append(s)
                    ans=max(ans,len(s))
        return ans