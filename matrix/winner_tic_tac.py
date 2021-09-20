class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        tic=[['','',''] for i in range(3)]
        for i in range(len(moves)):
            if i%2==0:
                tic[moves[i][0]][moves[i][1]]='A'
            else:
                tic[moves[i][0]][moves[i][1]]='B'
        def row(letter):
            count=0
            flag=False
            for i in range(len(tic)):
                for j in range(len(tic)):
                    if letter==tic[i][j]:
                        count+=1
                if count==3:
                    return True
                else:
                    count=0
            return False
        def col(letter):
            count=0
            for i in range(len(tic)):
                for j in range(len(tic)):
                    if letter==tic[j][i]:
                        count+=1
                if count==3:
                    return True
                else:
                    count=0
            return False
        def diag(letter):
            return (letter == tic[0][0] and letter==tic[1][1] and letter==tic[2][2]) or  (letter == tic[0][2] and letter==tic[1][1] and letter==tic[2][0])
        
        if row('A') or col('A') or diag('A'):
            return 'A'
        elif row('B') or col('B') or diag('B'):
            return 'B'
        else:
            if len(moves)==9:
                return 'Draw'
            else:
                return 'Pending'
    
        