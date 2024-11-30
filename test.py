board = []
height = 20
width = 20

board.append(['#'] * (width + 2))

for i in range(height):
    row = []
    row.append('#')
    for j in range(width):
        row.append(' ')
    row.append('#')
    board.append(row)

board.append(['#'] * (width + 2))
for row in board:
    for item in row:
        print(item, end='')
    print()