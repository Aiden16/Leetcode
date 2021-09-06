class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k==1:
            ans=s
            lis=list(s)
            for i in range(len(lis)):
                lis.append(lis[0])
                del lis[0]
                ans=min(ans,''.join(lis))
            return ans
        else:
            return ''.join(sorted(s))
