class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        row,col=len(image),len(image[0])
        color=image[sr][sc]
        if color==newColor:
            return image
        def dfs(r,c):
            if image[r][c]==color:
                image[r][c]=newColor
                #check in all 4 directiion
                if r>=1:dfs(r-1,c) #go up
                if r+1<row:dfs(r+1,c) #go down
                if c>=1:dfs(r,c-1) #go left
                if c+1<col:dfs(r,c+1) #go right
        dfs(sr,sc)
        return image
            
        