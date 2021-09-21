class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels=['a','e','i','o','u']
        ans=0
        left=0
        win=''
        v=0
        for char in range(k):
            win+=s[char]
            if s[char] in vowels:
                v+=1
        ans=max(ans,v)
        for char in range(len(s)-k):
            win+=s[char+k]
            if s[char] in vowels:
                v-=1
            if s[char+k] in vowels:
                v+=1
            ans=max(ans,v)
        return ans
 
        