'''
To find next greatest element
space complexity : O(n)
Time complexity : O(n^2)

'''

def monotonic_decreasing(arr):
    nge=[0]*len(arr)
    stack=[]
    for i in range(len(arr)):
        while stack and arr[stack[-1]]<arr[i]:
            nge[stack.pop()]=arr[i]
        stack.append(i)
    return nge
arr=list(map(int,input().split(' ')))
print(monotonic_decreasing(arr))
                