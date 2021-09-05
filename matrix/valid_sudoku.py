class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #using hashSet
        rows=collections.defaultdict(set)
        cols=collections.defaultdict(set)
        mat=collections.defaultdict(set)
        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col]=='.':
                    continue
                if (board[row][col] in rows[row] or
                    board[row][col] in cols[col] or
                    board[row][col] in mat[(row//3,col//3)]):
                    return False
                rows[row].add(board[row][col])
                cols[col].add(board[row][col])
                mat[(row//3,col//3)].add(board[row][col])
        return True
        #need hashin for col and row and 3X3
        #used array
        # rowHash={}
        # colHash={}
        # matHash={}
        # cols = collections.defaultdict(set)
        # for row in range(len(board)):
        #     for col in range(len(board)):
        #         if board[row][col]=='.':
        #             continue
        #         if row not in rowHash:
        #             rowHash[row]=[]
        #         if col not in colHash:
        #             colHash[col]=[]
        #         if (row//3,col//3) not in matHash:
        #             matHash[(row//3,col//3)]=[]
        #         if (board[row][col] in rowHash[row] or 
        #             board[row][col] in colHash[col] or
        #             board[row][col] in matHash[(row//3,col//3)]):
        #             return False
        #         rowHash[row].append(board[row][col])
        #         colHash[col].append(board[row][col])
        #         matHash[(row//3,col//3)].append(board[row][col])
        # return True
            