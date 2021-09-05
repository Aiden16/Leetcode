class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        hash={}
        for i in s:
            if i in hash:
                hash[i]+=1
            else:
                hash[i]=1
        new=''
        stack=[]
        p=0
        for i in t:
            if p<=len(s)-1:
                if i==s[p] and stack.count(i)!=hash[i]:
                    stack.append(i)
                    p+=1
            else:
                break
        return ''.join(stack)==s
      