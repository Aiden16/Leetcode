class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        ans=list(words[0])
        for word in words:
            check=[]
            for c in word:
                if c in ans:
                    check.append(c)
                    ans.remove(c)
            ans=check
        return ans
            