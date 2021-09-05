s='aab'
stack=[]
# c=0
# for i in s:
#     if not stack:
#         stack.append(i)
#     if stack[-1]==i:
p1=0
p2=1
new=''
c=0
while p2!=len(s):
    if s[p1]!=s[p2]:
        new+=s[p1]
        p1+=1
        p2+=1
    else:
        while s[p1]==s[p2]:
            c+=1
            p2+=1
    if c>=2:
        new+=s[p1]*2
        p2+=1
        p1=p2-1
    else:
        new+=s[p1]
        p1+=1
        p2+=1
    c=0
# new+=s[p1]
print(new)




class Solution:
    def makeFancyString(self, s: str) -> str:
        lc = None
        count = 0
        ans = []
        for c in s:
            if c != lc:
                lc = c
                count = 1
            elif count >= 2:
                continue
            else:
                count += 1
            ans.append(c)
        return ''.join(ans)