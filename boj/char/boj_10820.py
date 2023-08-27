import sys
lines = sys.stdin.readlines()
# line.input()
for s in lines:
    lower = 0
    upper = 0
    number = 0
    blank = 0

    for i in s:
        x = ord(i)
        if ord('A') <= x <= ord('Z'):
            upper = upper+1
        elif ord('a') <= x <= ord('z'):
            lower = lower+1
        elif ord('0') <= x <= ord('9'):
            number = number+1
        elif i == ' ':
            blank = blank+1

    print('%d %d %d %d' % (lower, upper, number, blank))
