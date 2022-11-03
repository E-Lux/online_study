from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())

pan = [list(map(int, input())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

q = deque()
q.append((0,0))
visited[0][0] = pan[0][0]

while q:
    x, y = q.popleft()

    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]

        if 0 <= new_x < n and 0 <= new_y < m and pan[new_x][new_y] != 0:
            if visited[new_x][new_y] == 0:
                visited[new_x][new_y] = visited[x][y] + pan[new_x][new_y]
                q.append((new_x, new_y))
            
            else:
                if visited[new_x][new_y] > visited[x][y] + pan[new_x][new_y]:
                    visited[new_x][new_y] = visited[x][y] + pan[new_x][new_y]
                    q.append((new_x, new_y))
                
print(visited[n-1][m-1])