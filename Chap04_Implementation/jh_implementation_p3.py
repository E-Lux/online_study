from itertools import combinations

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

home = []
chicken = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            home.append([i, j])
        elif graph[i][j] == 2:
            chicken.append([i, j])
            
data = list(combinations(chicken, m))
result = []
for d in range(len(data)):
    len_list1 = []
    for h in home:
        len_list2 = []
        for mm in range(m):
            li = data[d][mm]
            len_list2.append(abs(h[0] - li[0]) + abs(h[1] - li[1]))
        len_list1.append(min(len_list2))
    result.append(sum(len_list1))
    
print(min(result))