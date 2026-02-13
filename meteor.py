import turtle as t
import random
px=0
py=-100
mx=0
my=100
score = 0
meteors = []
c = 0
t.bgcolor("light blue")
t.title("meteor rain")
t.setup(450, 450)
t.hideturtle()
t.tracer(0, 0)
for _ in range(10):
    f = random.randint(-10, 9)
    c +=10
    meteors.append({
        "mx": f*20,
        "my": c*20
    })
t.pendown()
def square():
    for x in range(4):
        t.forward(20)
        t.right(90)
def player():
    t.pencolor("black")
    t.fillcolor("black")
    t.goto(px, py)
    t.pendown()
    t.begin_fill()
    square()
    t.end_fill()
    t.penup()

def meteor():
    for x in meteors:
        if x["my"] > 180:
            x["my"] = random.randint(1, 10) * 20
        if 200 < x["mx"] < -180:
            x["mx"] = random.randint(-10, 9) * 20
        t.pencolor("orange")
        t.fillcolor("orange")
        t.goto(x["mx"], x["my"])
        t.pendown()
        t.begin_fill()
        square()
        t.end_fill()
        t.goto(x["mx"], x["my"]+20)
        t.pencolor("red")
        t.fillcolor("red")
        t.begin_fill()
        square()
        t.end_fill()
        t.penup()

def logic():
    global mx, my, score, px, py
    for x in meteors:
        x["my"] -= 20
        if x["mx"] == px and x["my"] == py:
            score=0
            x["mx"] = (random.randint(-10,9))*20
            x["my"] = 200
            
        if (x["my"] <= -200):
            score += 1
            x["mx"] = (random.randint(-10,9))*20
            x["my"] = 200
    t.goto(-150, -180)
    t.pencolor("red")
    t.write(f"score{score}",font=("Arial", 8, "normal"))
    t.goto(200, 200)
    t.pendown()
    t.goto(-200, 200)
    t.goto(-200, -200)
    t.goto(200, -200)
    t.goto(200, 200)
    t.penup()

def left():
    global px
    if px > -200:
        px -= 20
def right():
    global px
    if px < 200:
        px += 20

def touch(x, y):
    if x < 0:
        left()
    elif x > 0:
        right()
t.onkeypress(left, "a")
t.onkeypress(right, "d")
t.onscreenclick(touch)
t.listen()
def mainloop():
    t.clear()
    player()
    meteor()
    logic()
    t.update()
    t.ontimer(mainloop, 100)
mainloop()
t.mainloop()
