def maximumSum (n, m, arr) : 
    #Complete the function
    ans = 0
    track = float('-inf')
    for i in range(len(arr)-1,-1,-1):
        if i == len(arr)-1:
            ans+=max(arr[i])
            track = max(arr[i])
            continue
        else:
            ins = float('-inf')
            for k in arr[i]:
                if k > ins and k<track:
                    ins = k
            if ins == float('-inf'):
                return 0
            else:
                ans+=ins
                track = ins
    return ans