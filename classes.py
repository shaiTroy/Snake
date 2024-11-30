import queue

class Snake:   
    def init(self, height, width):
        self.x = width
        self.y = height
        self.body = queue.Queue()
        self.body.put((width, height))
        self.direction = 'up'
    
    def append(self, x, y):
        self.body.put((x, y))
        
    def pop(self):
        return self.body[1:]
        
class Apple:
    def init(self, height, width):
        self.x = width
        self.y = height
        
class Board:
    def init(self, height, width):
        board = []
        
        #creating the board
        board.append(['#'] * (width + 2))

        for i in range(height):
            row = []
            row.append('#')
            for j in range(width):
                row.append(' ')
            row.append('#')
            board.append(row)

        board.append(['#'] * (width + 2))
        self.board = board
        
    
class Game:
    def init(self, height, width):
        self.height = height
        self.width = width
        self.snake = Snake(round(height/2), round(width/2))
        self.board = Board(height, width)
    
    def init_board(self):
        board = []
        self.board.append(['#'] * (self.width + 2))

        for i in range(self.height):
            row = []
            row.append('#')
            for j in range(self.width):
                row.append(' ')
            row.append('#')
            self.board.append(row)

        self.board.append(['#'] * (self.width + 2))

        return self.board
    
    def printBoard(self):
        board = self.board()
        for row in board:
            for item in row:
                print(item, end='')
            print()
    
    def render(self):
        board = self.board()
        