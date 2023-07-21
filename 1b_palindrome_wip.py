# TODO

from collections import Counter

def is_palindrome(s):
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True

while True:
    try:
        best = ''
        for s in map(lambda x: x if x.isalnum() else ' ', raw_input()).split(' '):
            if len(best) < len(s) and is_palindrome(s):
                best = s
    except:
        break
