class Solution:
    def judgeCircle(self, moves: str) -> bool:
        h={}
        for i in moves:
            h[i]=h.get(i,0)+1
        L=h.get('L')
        R=h.get('R')
        D=h.get('D')
        U=h.get('U')
        if L==R and U==D:
            return True
        return False