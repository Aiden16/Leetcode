class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        check='ballon'
        hash={}
        for i in text:
            if i in check:
                hash[i]=hash.get(i,0)+1
        flag=0
        if 'b' in hash and 'a' in hash and 'l' in hash and 'o' in hash and 'n' in hash:
            flag=1
            ans=min(hash['b'],hash['a'],hash['l']//2,hash['o']//2,hash['n'])
            return ans
        return 0
        