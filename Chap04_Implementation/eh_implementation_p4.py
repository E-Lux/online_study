# 규칙만 찾으면 쉽게 풀림
# 규칙도 쉬운편

import sys

input = sys.stdin.readline
INF = int(1e9)

# 방향: 오 위 왼 아 => 이 순서로 커브 돈다
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
check = [[False] * 101 for _ in range(101)]

n = int(input())

x_max = -1
y_max = -1

ans = 0

for _ in range(n):
    x, y, d, th = map(int, input().split()) # x, y 좌표 바꿔야 나한테 익숙한 좌표로 바뀜 
    x, y = y, x
    check[x][y] = True

    x_max = max(x_max, x)
    y_max = max(y_max, y) 

    order_arr = []
    nx = x + dx[d]
    ny = y + dy[d]


    if 0 <= nx <= 100 and 0 <= ny <= 100:
        check[nx][ny] = True # 0세대 값 그음
        x = nx
        y = ny
        order_arr.append(d)
        d = (d + 1) % 4
    
        x_max = max(x_max, x)
        y_max = max(y_max, y) 
    
    for _ in range(th): # 세대 수 만큼 반복
        tmp = []
  
        for i in range(len(order_arr) - 1, -1, -1):
            p = order_arr[i]
            p = (p + 1) % 4

            nx = x + dx[p]
            ny = y + dy[p]

            if 0 <= nx <= 100 and 0 <= ny <= 100:
                check[nx][ny] = True
                tmp.append(p)
                x = nx
                y = ny
           
                x_max = max(x, x_max)
                y_max = max(y, y_max)
    
        order_arr.extend(tmp)



for i in range(x_max+1):
    for j in range(y_max+1):
        if 0 <= i <= 100 and 0 <= j <= 100:
            if check[i][j]:
                if j + 1 <= 100 and i + 1 <= 100:
                    if check[i][j+1] and check[i+1][j+1] and check[i+1][j]:
                        ans += 1

print(ans)