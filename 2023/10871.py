import sys
sys.stdin = open("input.txt","rt")

n,x = map(int,input().split())
a=list(map(int,input().split()))

for i in a:
    if i<x:
        print(i,end=' ')