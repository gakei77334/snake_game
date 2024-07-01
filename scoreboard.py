from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 18, "normal")

class ScoreBoard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:  # Open file in read-only mode using "with"
            self.high_score = int(data.read())  # Read the contents in data.txt file and convert from string to integer
        self.contents = self.high_score
        self.color("white")
        self.penup()
        self.goto(0, 270)        
        self.hideturtle()
        self.score_counter()
                
        
    def score_counter(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)
        
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:  # Open file in write mode
                data.write(f"{self.high_score}") # Replaces content in data.txt file with new high_score
        self.score = 0
        self.score_counter()
        
    def increase_score(self):
        self.score += 1
        self.score_counter()
        
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)
        
        
###### Professor Code ######
# She makes a separate function that updates/writes the new score on the scoreboard

# class ScoreBoard(Turtle):
    
#     def __init__(self):
#         super().__init__()
#         self.score = 0
#         self.color("white")
#         self.penup()
#         self.goto(0, 270)        
#         self.hideturtle()
#         self.update_scoreboard()
    
#     def update_scoreboard():
#         self.write(arg=f"Score: {self.score}", align="center", font=("Arial", 18, "normal"))
        
#     def counter(self):
#         self.score += 1  
#         self.clear()
#         self.update_scoreboard()

