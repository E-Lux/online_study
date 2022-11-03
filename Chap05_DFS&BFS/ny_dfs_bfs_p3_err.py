import sys
N,M = map(int,sys.stdin.readline().split())
arr = [[] for i in range(N)]
for i in range(M):
    a, b = map(int,sys.stdin.readline().split())
    arr[a].append(b)
    arr[b].append(a)

def dfs(x,d):
    #print('dfs',x,d)
    visited[x] =1
    if d == 5:
        print(1)
        exit()

    for y in arr[x]:
        if visited[y] == 1:
            continue
        dfs(y,d+1)


for i in range(N):
    visited = [0 for i in range(N)]
    depth = 1
    dfs(i,depth)

print(0)
