s = input().split()
whites = []
if len(s) > 1:
    whites = s[1].split(',')
s = input().split()
blacks = []
if len(s) > 1:
    blacks = s[1].split(',')
board = [['...', ':::', '...', ':::', '...', ':::', '...', ':::'],
         [':::', '...', ':::', '...', ':::', '...', ':::', '...'],
         ['...', ':::', '...', ':::', '...', ':::', '...', ':::'],
         [':::', '...', ':::', '...', ':::', '...', ':::', '...'],
         ['...', ':::', '...', ':::', '...', ':::', '...', ':::'],
         [':::', '...', ':::', '...', ':::', '...', ':::', '...'],
         ['...', ':::', '...', ':::', '...', ':::', '...', ':::'],
         [':::', '...', ':::', '...', ':::', '...', ':::', '...']]
r = 'abcdefgh'
for c in whites:
    if len(c) < 3:
        c = 'P' + c
    x = r.index(c[1])
    y = 8-int(c[2])
    s = board[y][x]
    board[y][x] = s[0]+c[0].upper()+s[2]
for c in blacks:
    if len(c) < 3:
        c = 'P' + c
    x = r.index(c[1])
    y = 8-int(c[2])
    s = board[y][x]
    board[y][x] = s[0]+c[0].lower()+s[2]
print("+---+---+---+---+---+---+---+---+")
for row in board:
    print('|' + '|'.join(row) + '|')
    print("+---+---+---+---+---+---+---+---+")
