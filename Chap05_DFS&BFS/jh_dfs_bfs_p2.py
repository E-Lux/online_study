n, m = map(int, input().split())
cnt = 1

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))
    
x = 0
y = 0
while True:
    if x == n-1 and y == m-1:
        break
    
    if y < m-1 and graph[x][y+1] == 1:
        y += 1
        cnt += 1
    elif x < n-1 and graph[x+1][y] == 1:
        x += 1
        cnt += 1
        
print(cnt)