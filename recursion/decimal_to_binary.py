def dec_to_bin(decimal,result):
    if decimal==0:
        return result
    result=str(decimal%2)+result
    return dec_to_bin(decimal//2,result)
print(dec_to_bin(6,""))