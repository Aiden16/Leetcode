def diagonalDifference(arr):
    # Write your code here
    rightDia=0
    leftDia=0
    j=len(arr[0])-1
    for i in range(len(arr)):
        rightDia+=arr[i][i]
        leftDia+=arr[i][j]
        j-=1
    return abs(rightDia-leftDia)