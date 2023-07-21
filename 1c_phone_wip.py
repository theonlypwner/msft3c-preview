# TODO
import re



def alphaToNum(c):
    if not c.isalpha():
        return c
    return str((2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7, 8, 8 ,8, 9, 9, 9, 9)[ord(c.lower())-ord('a')])

def process(s):
    s = str(map(alphaToNum, s))
    m = re.match(r'(?:+?1)?', s)
    if m:
    m = re.match(r'1-([0-9]{3}-[0-9a-zA-Z-]+)', s)
    if m:
    return None

while True:
    try:
        print(process(raw_input()) or 'Fleshling follow-up needed')
    except:
        break
