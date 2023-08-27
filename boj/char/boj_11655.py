import sys
def input(): return sys.stdin.readline().strip()


s = input()

lowa = ord('a')
lowz = ord('z')
uppera = ord('A')
upperz = ord('Z')
result = ''

for i in s:
    t = ord(i)+13
    if (lowa <= ord(i) <= lowz):
        if t > lowz:
            result += chr(((t % (lowa+26))+lowa))
        else:
            result += chr(t)
    elif (uppera <= ord(i) <= upperz):
        if t > upperz:
            result += chr((t % (uppera+26))+uppera)
        else:
            result += chr(t)
    else:
        result += i
print(result)
