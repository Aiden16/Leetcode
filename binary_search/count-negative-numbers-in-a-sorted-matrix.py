class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        #binary_search
        def func(row):
            f,e=0,len(row)
            while f<e:
                mid=(f+e)//2
                if row[mid]<0:
                    e=mid
                else:
                    f=mid+1
            return len(row)-f
        count=0
        for i in grid:
            count+=func(i)
        return count
    
    #brute force
        count=0
        for i in range(len(grid)):
            for j in range(len(grid[i])-1,-1,-1):
                if grid[i][j]<0:
                    count+=1
        return count
        