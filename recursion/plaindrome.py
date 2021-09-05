def isPalindrome(string):
    if len(string)==1 or len(string)==0:
        return True
    if string[0]==string[-1]:
        return isPalindrome(string[1:len(string)-1])
    else:
        return False
print(isPalindrome('nitin'))