
def test(n):
    # if n<1:
    #     return 0
    # else:
    #     test(n-1)
    #     print(n)
    # s=3
    s=0
    if n==0:
        return 0
    s=n+test(n-1)
    print(s)
    return s
print(test(3))