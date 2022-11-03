n, m = map(int, input().split())
cnt = 0

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))
    
def dfs(graph, x, y):
    graph[x][y] = 1
    
    if x > 0:
        if graph[x-1][y] == 0:
            dfs(graph, x-1, y)
    if x < n-1:
        if graph[x+1][y] == 0:
            dfs(graph, x+1, y)
    if y > 0:
        if graph[x][y-1] == 0:
            dfs(graph, x, y-1)
    if y < m-1:
        if graph[x][y+1] == 0:
            dfs(graph, x, y+1)
    
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            dfs(graph, i, j)
            cnt += 1
            
print(cnt)