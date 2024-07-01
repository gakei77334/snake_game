from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    
    def __init__(self):
        self.all_squares = []
        self.create_snake()        
        self.head = self.all_squares[0]
        
    
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_square(position)
            
            
    def add_square(self, position):
        new_square = Turtle("square")
        new_square.color("white")
        new_square.penup()
        new_square.goto(position)
        self.all_squares.append(new_square)  
        
        
    def reset(self):
        for square in self.all_squares:
            square.goto(1000, 1000)
        self.all_squares.clear()
        self.create_snake()
        self.head = self.all_squares[0]
        
          
    def extend(self):
        self.add_square(self.all_squares[-1].position())
        
            
    def move(self):
        for square_num in range(len(self.all_squares) - 1, 0, -1):
            new_x = self.all_squares[square_num - 1].xcor()
            new_y = self.all_squares[square_num - 1].ycor()
            self.all_squares[square_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
        
        
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
            
        
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
            
        
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
            
        
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

