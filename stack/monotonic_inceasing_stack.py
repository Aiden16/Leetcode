'''
To find next smaller element
space complexity : O(n)
Time complexity : O(n^2)

'''

def monotonic_decreasing_stack(arr):
    nse=[0]*len(arr)
    stack=[]
    for i in range(len(arr)):
        while stack and arr[stack[-1]]>arr[i]:
            nse[stack.pop()]=arr[i]
        stack.append(i)
    return nse
arr=list(map(int,input().split(' ')))
print(monotonic_decreasing_stack(arr))