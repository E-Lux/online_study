n, m = map(int, input().split())
x, y, d = map(int, input().split())

pan = list(map(int, input().split()) for _ in range(n))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

ans = 0

while True:
    
    if pan[x][y] == 0: # (x,y) 방문 처리 => 방문 노드 값 2로 설정
        pan[x][y] = 2
        ans += 1
  
    check = True # 현재 위치에서 동서남북 중에 방문한 곳이 없다면 뒤로 가기 위해 필요
    nd = d

    for _ in range(4):
        nd -= 1 # 탐색 시작 # 주어진 방향의 왼쪽부터 탐색한다 => d = 1 (동쪽일 때): 0(북) -> 3(서) -> 2(남) -> 1(동) 순으로 탐색함 => d -= 1 되면 됨
        if nd == -1:
            nd = 3
    
        nx = x + dx[nd]
        ny = y + dy[nd]

        if pan[nx][ny] == 0: # 탐색한 곳이 방문하지 않은 곳이라면 위치를 옮김
            d = nd
            x = nx
            y = ny 
            check = False # 현재 위치에서 방문 할 곳이 있으므로 뒤로가지 않아도 됨
            break
    
    if check:# 만약 현재 위치 4면 탐색 끝내고 방문 할 곳이 없다면 뒤로 가야함
        nx = x + dx[(d + 2) % 4]
        ny = y + dy[(d + 2) % 4]

        if pan[nx][ny] == 1: # 옮긴 곳이 벽이라면 끝
            break
        else:
            x = nx
            y = ny

print(ans)