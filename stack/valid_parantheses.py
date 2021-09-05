class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        comb={'(':')','{':'}','[':']'}
        for brkt in s:
            if brkt in comb.keys():
                stack.append(brkt)
            else:
                if len(stack)>0 and comb[stack[-1]]==brkt:
                    stack.pop()
                else:
                    return False
        return len(stack)==0