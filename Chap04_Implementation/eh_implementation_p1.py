pos = input()

x = int(pos[1])
y = ord(pos[0]) - 96 # a~h를 숫자 좌표로 바꾸기 위해 

cnt = 0
d = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -1), (1, 2)]

for nx, ny in d:
    if 1 <= x + nx <= 8 and 1 <= y + ny <= 8: 
        cnt += 1

print(cnt)
