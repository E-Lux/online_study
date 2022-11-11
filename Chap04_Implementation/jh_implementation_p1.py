loc = input()

if loc in ['a1', 'a8', 'h1', 'h8']:
    answer = 2
elif loc in ['a2', 'a7', 'b1', 'b8', 'g1', 'g8', 'h2', 'h7']:
    answer = 3
elif (ord('c') <= ord(loc[0]) <= ord('f')) and (3 <= loc[1] <= 6):
    answer = 8
else:
    if loc[0] == 'a' or loc[0] == 'h' or loc[1] == 1 or loc[8]:
        answer = 4
    else:
        if loc in ['b2', 'b7', 'g2', 'g7']:
            answer = 4
        else:
            answer = 6
            
print(answer)