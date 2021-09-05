class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        counter=0
        lis=[]
        lis[0:]=s
        if s==goal:
            return True
        while counter!=len(s)-1:
            a=lis.pop(0)
            lis.append(a)
            if ''.join(lis)==goal:
                return True
            counter+=1
        return False