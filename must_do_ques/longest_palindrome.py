class Solution:
    def longestPalindrome(self, s: str) -> int:
        pairs=0
        chars=set()
        for char in s:
            if char in chars:
                pairs+=1
                chars.remove(char)
            else:
                chars.add(char)
        return pairs*2+1 if chars else pairs*2
         
                
#own soln

class Solution:
    def longestPalindrome(self, s):
        ans = 0
        hash={}
        for i in s:
            hash[i]=hash.get(i,0)+1
        print(hash)
        for i in hash.keys():
            if hash[i]%2==0:
                ans+=hash[i]
            elif hash[i]!=1:
                ans+=(hash[i]//2)*2
        return ans if ans==len(s) else ans+1
        # return ans