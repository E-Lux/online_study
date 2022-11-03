import sys
from collections import deque
N,M = map(int,input().split())
arr = []
for i in range(N):
    x= list(map(int,input().rstrip()))
    arr.append(x)
dx=[-1,0,1,0]
dy=[0,1,0,-1]
#print(arr)
q= deque()
q.append((0,0))
arr[0][0] = 2
while q:
    x,y= q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<= nx < N and 0<= ny < M:
            if arr[nx][ny] ==1:
                arr[nx][ny] = arr[x][y] +1
                q.append((nx,ny))

print(arr[N-1][M-1]-1)
