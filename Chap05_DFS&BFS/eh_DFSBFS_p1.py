n, m = map(int, input().split())

pan = [input() for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[0] * m for _ in range(n)]
cnt = 0

def solve(x, y):

    visited[x][y] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and pan[nx][ny] == '0' and visited[nx][ny] == 0:
            solve(nx, ny)

for x in range(n):
    for y in range(m):
        if pan[x][y] == '0' and visited[x][y] == 0:
            solve(x, y)
            cnt += 1

print(cnt)