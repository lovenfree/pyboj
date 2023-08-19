import sys
sys.stdin=open("2_input.txt","rt")

def dfs(sum,day):
   global max
  
   if day == n+1:
       
    if sum>max:
      max = sum
   else:
        if day+times[day]<=n+1:
            dfs(sum+points[day], day+times[day])
        dfs(sum, day+1)

if __name__ == "__main__":
    n = int(input())
  
    times = list()
    points = list()

    max = 0

    for i in range(n):
      t, p = map(int, input().split())
      times.append(t)
      points.append(p)

    times.insert(0,0)
    points.insert(0,0)
    dfs(0,1)
    print(max)
        

        
