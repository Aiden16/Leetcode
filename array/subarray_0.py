from typing import Hashable


def sub(arr):
    hash = {arr[0]:[0]}
    sum=arr[0]
    ans=[]
    for i in range(1,len(arr)):
        sum+=arr[i]
        if sum==0:
            ans.append((0,i))
        if sum not in hash:
            hash[sum]=[i]
        else:
            for j in hash[sum]:
                ans.append((j+1,i))
            hash[sum].append(i)
    print(hash)
    return ans
arr=[4,5,-3,-2]
print(sub(arr))
print('=============================================')
arr2=[6, 3, -1, -3, 4, -2, 2, 4, 6, -12, -7]
print(sub(arr2))

