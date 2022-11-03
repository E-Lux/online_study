n, m = map(int, input().split())

graph = [[] for _ in range(n)]
check = False

for _ in range(m):
    a, b = map(int, input().split())

    graph[a].append(b) 
    graph[b].append(a)


for i in range(n):
    stack = []
    stack.append([i, 1, str(i)])


    while stack:
        val, cnt, visited = stack.pop()

        if cnt >= 5:
            check = True
            break

        for i in graph[val]:
            if str(i) not in visited:
                stack.append([i, cnt + 1, visited+str(i)])
            

if check:
    print(1)
else:
    print(0)