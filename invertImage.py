mat = []
n=int(input())
for i in range(n):
    temp=list(map(int,input().split(' ')))
    mat.append(temp)
print(mat)
for i in range(len(mat)):
    mat[i] = mat[i][::-1]
    print(mat[i])

    for j in range(len(mat[i])):
        if mat[i][j]==0:
            # print('lalla00000')

            mat[i][j]=1
        else:
            # print('lalla11111')

            mat[i][j]=0
    # for i in range(len(mat)):
    #     for j in range(len(mat[i])):
    #         if mat[i][j]==0:
    #             mat[i][j]=1
    #         else:
    #             mat[i][j]=0
print(mat)