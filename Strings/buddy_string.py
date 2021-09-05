class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        #optimized soln
        if len(s)!=len(goal):
            return False
        if s==goal:
            return True if len(s)-len(set(s))>=1 else False
        diff=[]
        for i in range(len(s)):
            if s[i]!=goal[i]:
                diff.append(i)
            if len(diff)>2:
                return False
        if len(diff)!=2:
            return False
        if s[diff[0]]==goal[diff[1]] and s[diff[1]]==goal[diff[0]]:
            return True
        return False
#         if len(s)==1 and len(goal)==1:
#             return False
            
#         if s.count(s[0])==len(s) and s==goal:
#             return True
#         p1=0
#         p2=0
#         index=[]
#         h1={}
#         h2={}
#         while p1<len(s) and p2<len(goal):
#             h1[s[p1]]=h1.get(s[p1],0)+1
#             h2[goal[p2]]=h2.get(s[p2],0)+1
#             if s[p1]!=goal[p2]:
#                 index.append(p1)
#             p1+=1
#             p2+=1
#         if len(index)==2:
#             s=list(s)
#             s[index[0]],s[index[1]]=s[index[1]],s[index[0]]
#             return ''.join(s)==goal
#         elif len(index)==0 and len(s)>2:
#             # return True
#             for val in h1.values():
#                 if val>1:
#                     return True
#             return False
#         return False

        