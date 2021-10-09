class Solution:
    def mostCommonWord(self, p: str, b: List[str]) -> str:
        n=''.join([c.lower() if c.isalnum() else ' ' for c in p])
        lis=n.split(' ')
        hash={}
        max_freq=0
        ans=''
        for i in lis:
            if i not in b and i!='':
                hash[i]=hash.get(i,0)+1
                if hash[i]>max_freq:
                    max_freq=hash[i]
                    ans=i
        return ans
    