def twod(a,m,n):
    new=[]
    i=0
    # print('--------',new[0][2])
    # print(new[1][0])
    for row in range(0,m):
        temp=[]
        for col in range(0,n):
            # print('===>',row,col)
            # print(a[i])
            # print('vefore',new[row][col],row,col)
            temp.append(a[i])
            # print('after',new[row][col],row,col)

    #         print(new)
            i+=1
        print(temp)
        new.append(temp)
    return new
print(twod([1,2,3,4],2,2))