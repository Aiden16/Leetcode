def min_ele(a):
    min_so_far=a[0]
    cur_min = a[0]
    for i in range(1,len(a)):
        cur_min=min(min_so_far,abs(min_so_far-a[i]))
        min_so_far = min(min_so_far,cur_min)
    return min_so_far
lis=[543,384,652,445,699]
print(min_ele(lis))