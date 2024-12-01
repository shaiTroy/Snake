import random
class Snake:   
    def __init__(self):
        self.body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]
              ]
        self.direction = 'RIGHT'
        self.position = [100, 50]
        
class Apple:
    def __init__(self, window_x, window_y):
        self.window_x = window_x
        self.window_y = window_y
        self.position = [random.randrange(1, (self.window_x//10)) * 10, random.randrange(1, (self.window_y//10)) * 10]
        
    def randomApple(self):
        self.position = [random.randrange(1, (self.window_x//10)) * 10, random.randrange(1, (self.window_y//10)) * 10]