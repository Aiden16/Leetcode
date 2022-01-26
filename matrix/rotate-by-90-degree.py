def rotate(mat): 
    #code here
    # mat = []
    #take transpose
    for row in range(len(mat)):
        for col in range(row,len(mat)):
            mat[row][col],mat[col][row] = mat[col][row],mat[row][col]
    #now reverse rows
    p1,p2=0,len(mat)-1
    while p1<=p2:
        mat[p1],mat[p2] = mat[p2],mat[p1]
        p1+=1
        p2-=1