from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 18, 'normal')


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as high_score:
            self.high_score = int(high_score.read())
        self.color("White")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.clear()
        self.write(f"Score : {self.score} High Score : {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            with open("data.txt", "w") as score_file:
                score_file.write(str(self.score))
        self.score = 0
        self.update_score()
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game Over", align=ALIGNMENT, font=FONT)

    def calculate_score(self):
        self.score += 1
        self.update_score()
