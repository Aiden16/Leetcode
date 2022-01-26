class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stck  = []
        for i in range(len(s)):
            if not stck:
                stck.append([s[i],1])
                continue
            if stck[-1][0] == s[i]:
                stck[-1][1]+=1
                if stck[-1][1]==k:
                    stck.pop()
            else:
                stck.append([s[i],1])
        ans=''
        for i in stck:
            ans += i[0]*i[1]
        return ans