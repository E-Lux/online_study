
N,M = map(int,input().split())
arr = []
for i in range(N):
    arr.append(list(map(int,input().rstrip())))


print(arr)
answer = 0
#상하좌우
dx=[-1,0,1,0]
dy=[0,1,0,-1]
def dfs(i,j,arr):
    arr[i][j] =2
    for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]
        if 0<= nx < N and 0<= ny < M :
            if arr[nx][ny] == 0:
                dfs(nx,ny,arr)



for i in range(N):
    for j in range(M):
        if int(arr[i][j]) ==0:
            dfs(i,j,arr)
            answer +=1
print(answer)
