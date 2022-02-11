class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        #using counter
        pc = Counter(p)
        sc = Counter(s[:len(p)])
        i,j=0,len(p)
        ans = []
        while j<len(s):
            if pc==sc:
                ans.append(i)
            sc[s[j]]+=1
            sc[s[i]]-=1
            if sc[s[i]] == 0:
                del sc[s[i]]
            i+=1
            j+=1
        if sc==pc:
            ans.append(i)
        return ans
        
        
#my own soln
        if len(s)<len(p):
            return []
        n=len(p)
        p = Counter(p)
        req = n
        h = 0
        win = {}
        for i in range(n):
            if s[i] in p and s[i] not in win:
                win[s[i]] = 1
                h += 1
            elif s[i] in win and s[i] in p and p[s[i]]>win[s[i]]:
                win[s[i]]+=1
                h+=1
            elif s[i] in win and s[i] in p:
                win[s[i]]+=1
        ans = []
        if h == req:
            ans.append(i-n+1)
        for i in range(n,len(s)):
            if s[i-n] in win:
                win[s[i-n]]-=1
                if win[s[i-n]]<p[s[i-n]]:
                    h-=1
                if win[s[i-n]]<=0:
                    del win[s[i-n]]
            if s[i] in p and s[i] not in win:
                win[s[i]] = 1
                h += 1
            elif s[i] in win and s[i] in p and p[s[i]]>win[s[i]]:
                win[s[i]]+=1
                h+=1
            elif s[i] in win and s[i] in  p:
                win[s[i]]+=1
            if h==req:
                ans.append(i-n+1)
        return ans

            