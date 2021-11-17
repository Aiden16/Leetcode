class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        iterate=set(s)
        h=defaultdict(list)
        for ind,char in enumerate(s):
            h[char].append(ind)
        ans=0
        for char in iterate:
            if len(h[char])>=2:
                ans+=len(set(s[h[char][0]+1:h[char][-1]]))
        return ans