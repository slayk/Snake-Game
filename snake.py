from turtle import Turtle

STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake():
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        newTurtle = Turtle("square")
        newTurtle.color("teal")
        newTurtle.penup()
        newTurtle.goto(position)
        self.segments.append(newTurtle)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for segment in range(len(self.segments)-1, 0, -1):
            newX = self.segments[segment - 1].xcor()
            newY = self.segments[segment - 1].ycor()
            self.segments[segment].goto(newX, newY)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def otherEnd(self):
        if self.head.xcor() > 280:
            yCor = self.segments[-1].ycor()
            self.head.goto(-280, yCor)
        elif self.head.xcor() < -280:
            yCor = self.segments[-1].ycor()
            self.head.goto(280, yCor)
        elif self.head.ycor() > 280:
            xCor = self.segments[-1].xcor()
            self.head.goto(xCor, -280)
        elif self.head.ycor() < -280:
            xCor = self.segments[-1].xcor()
            self.head.goto(xCor, 280)