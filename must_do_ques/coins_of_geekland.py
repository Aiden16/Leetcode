new = []
        for i in range(N):
            tmp = []
            for j in range(N):
                tmp.append(0)
            new.append(tmp)
        # print(new)
        row = 0
        while row<N:
            s=0
            for col in range(N):
                if col<k:
                    s+=mat[row][col]
                    new[row][col] = s
                else:
                    s+=mat[row][col]
                    s-=mat[row][col-k]
                    new[row][col] = s
                # print(s)
            # print(s)
            row+=1
        # print(new)
        
        ans = float('-inf')
        col = k-1
        while col<N:
            s = 0
            for row in range(N):
                # print('----',row,col,new[row][col])
                if row<k-1:
                    s+=new[row][col]
                elif row==k-1:
                    s+=new[row][col]
                    ans=max(ans,s)
                else:
                    s+=new[row][col]
                    s-=new[row-k][col]
                    ans=max(ans,s)
                # print(s)
            col+=1
        # print(ans)
        return ans
                