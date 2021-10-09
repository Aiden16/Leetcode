class Solution(object):
    def diagonalSort(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        #let us get all values of diagonal
        temp=[]
        hash={} #coord:diag_array
        visited=set()
        row=len(mat)
        col=len(mat[0])
        for r in range(row):
            for c in range(col):
                x=r
                y=c
                if (x,y) in visited:
                    continue
                while x<=row-1 and y<=col-1 and (x,y):
                    temp.append(mat[x][y])
                    visited.add((x,y))
                    x+=1
                    y+=1
                temp.sort()
                hash[(r,c)]=temp
                temp=[]
        for i in hash.keys():
            r,c=i
            for vals in hash[i]:
                mat[r][c]=vals
                r+=1
                c+=1
        return mat
