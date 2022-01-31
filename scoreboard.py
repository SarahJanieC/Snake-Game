from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
PATH = "/Users/SarahJC/Desktop/Python Projects/Snake Game/"
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open(f"{PATH}data.txt") as data:
            self.highscore = int(data.read())
        self.penup()
        self.color("white")
        self.goto(0,270)
        self.update_scoreboard()
        self.hideturtle()
        

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", False, align=ALIGNMENT, font=FONT)

    #def game_over(self):
    #    self.goto(0,0)
    #    self.write("GAME OVER", False, align=ALIGNMENT, font=FONT)
        
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open(f"{PATH}data.txt", mode="w") as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.update_scoreboard()