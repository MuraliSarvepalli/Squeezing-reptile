#palindrome

def palindrome(st):
    if st[::]==st[::-1]:
        return True
    else:
        return False

st=input('Enter the string')
print(palindrome(st))
