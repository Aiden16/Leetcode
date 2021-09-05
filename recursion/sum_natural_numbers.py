def sum_natural(number):
    if number==1:
        return 1
    return number+sum_natural(number-1)
print(sum_natural(10))