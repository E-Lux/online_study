n, m = map(int, input().split())
x, y, direc = map(int, input().split())
graph = []
visited = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
    visited.append([0] * m)
visited[x][y] = 1

steps = [[-1, 0], [0, 1], [1, 0], [0, -1]]
cnt = 1
turn_cnt = 0
while True:
    # 1.
    if direc == 0:
        direc = 3
    else:
        direc -= 1
    n_x = x + steps[direc][0]
    n_y = y + steps[direc][1]
    # 2-1.
    if graph[n_x][n_y] == 0 and visited[n_x][n_y] == 0:
        visited[n_x][n_y] = 1
        x = n_x
        y = n_y
        cnt += 1
        turn_cnt = 0
    # 2-2.
    else:
        turn_cnt += 1
    # 3.
    if turn_cnt == 4:
        n_x = x - steps[direc][0]
        n_y = y - steps[direc][1]
        # 3-1.
        if graph[n_x][n_y] == 0:
            x = n_x
            y = n_y
            turn_cnt = 0
        # 3-2.
        else:
            break
            
print(cnt)