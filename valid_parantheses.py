class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
    
        maping={'(':')','[':']','{':'}'}
        if s[0] in maping.values():
            return False
        stack=[s[0]]
        for i in range(1,len(s)):
            if len(stack)>0:
                if maping[stack[-1]]==s[i]:
                    stack.pop()
                else:
                    if s[i] in maping.values():
                        return False
                    stack.append(s[i])
            else:
                if s[i] in maping.values():
                    return False
                stack.append(s[i])
        if not stack:
            return True
        return False
        
        