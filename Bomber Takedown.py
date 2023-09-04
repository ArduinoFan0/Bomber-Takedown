print("Program begin!")
import turtle as t
print("Started turtle")
import time
from random import *
s = t.getscreen()

#variables
xvel = 0.0
yvel = 0.0
xthrust = 0.0
ythrust = 0.0
space_pressed = False
state = "Title screen"
laser_on = False
millis = 0
smillis = 0
laser_x = 0
laser_y = 0
bomb_x = 0
bomb_y = 3001
tower_1 = 10
tower_2 = 10
tower_3 = 10
smillis2 = 0
plane_x = 0
plane_y = 3001
bomb_placex = -900
bomb_xvel = 0
plane_yvel = 0
rep = 100
gameover_cause = ""
old_space_pressed = False
boom1_x = 0
boom1_y = 0
boom2_x = 0
boom2_y = 0
boom1_millis = 0
boom2_millis = 0
plane_left = True
score = 0
scrnsize = 1.0

#constants
friction = 0.69
collision_radius = 15
tower_floors = 6
aspectforx = 1.076923077
aspectfory = 0.928571428

print("variables declared")

def start_left():
    global xvel, yvel, xthrust, ythrust, friction
    xthrust = -8
def start_right():
    global xvel, yvel, xthrust, ythrust, friction
    xthrust = 8
def start_up():
    global xvel, yvel, xthrust, ythrust, friction
    ythrust = 8
def start_down():
    global xvel, yvel, xthrust, ythrust, friction
    ythrust = -8
def end_left():
    global xvel, yvel, xthrust, ythrust, friction
    if xthrust < 0:
        xthrust = 0
def end_right():
    global xvel, yvel, xthrust, ythrust, friction
    if xthrust > 0:
        xthrust = 0
def end_up():
    global xvel, yvel, xthrust, ythrust, friction
    if ythrust > 0:
        ythrust = 0
def end_down():
    global xvel, yvel, xthrust, ythrust, friction
    if ythrust < 0:
        ythrust = 0
def start_space():
    global space_pressed
    space_pressed = True
def end_space():
    global space_pressed
    space_pressed = False
def tower(x=int, y=int, width=int, height=int, floors=int, health=int, gunradius=20, gunlength=70, colx=None, coly=None):
    global laser_x, laser_y, scrnsize
    trueheight = height / floors
    top = height - trueheight * (floors - health)
    t.goto(x, y)
    t.pd()
    t.sety(y + top)
    t.pu()
    t.goto(x + width, y)
    t.pd()
    t.sety(y + top)
    t.pu()
    t.goto(x, y + top)
    t.pd()
    t.setx(x + width)
    t.pu()
    
    for n in range(0, health):
        t.pu()
        t.goto(x, y + n * trueheight)
        t.pd()
        t.seth(0)
        t.fd(width)
        t.pu()
        t.goto(x + width * 0.1, y + n * trueheight + (trueheight * 0.1))
        t.pd()
        t.seth(90)
        t.fd(trueheight / 1.2)
        t.seth(0)
        t.fd(width / 2.9)
        t.seth(270)
        t.fd(trueheight / 1.2)
        t.seth(180)
        t.fd(width / 2.9)
        t.pu()
        t.goto(x + width * 0.55, y + n * trueheight + (trueheight * 0.1))
        t.pd()
        t.seth(90)
        t.fd(trueheight / 1.2)
        t.seth(0)
        t.fd(width / 2.9)
        t.seth(270)
        t.fd(trueheight / 1.2)
        t.seth(180)
        t.fd(width / 2.9)
    t.pu()
    t.goto(x + width * 0.3, y + trueheight / 2)
    t.dot(round(4 * scrnsize))
    t.goto(x + width * 0.7, y + trueheight / 2)
    t.dot(round(4 * scrnsize))
    t.goto(x + width / 2, y + height - trueheight * (floors - health))
    t.seth(t.towards(laser_x, laser_y))
    t.pd()
    t.fd(gunlength)
    t.bk(gunlength)
    t.seth(0)
    t.fd(gunradius)
    t.seth(90)
    t.circle(gunradius, 180)
    if laser_on:
        t.goto(x + width / 2, y + height - trueheight * (floors - health))
        t.seth(t.towards(laser_x, laser_y))
        t.fd(gunlength)
        t.pencolor("red")
        t.goto(laser_x, laser_y)
    t.pu()
    t.pencolor("black")
    if (colx != None) and (coly != None):
        if((colx > x) and (colx < (x + width))) and ((coly > y) and (coly < (y + top))):
            return True
    return False
def boom(x=int, y=int):
    global millis
    t.goto(x,y)
    t.seth(millis * 1)
    t.pd()
    t.circle(9)
    t.rt(69)
    t.circle(25)
    t.rt(69)
    t.circle(15)
    t.rt(69)
    t.pu()

def init():
    global smillis, tower_1, tower_2, tower_3, tower_floors
    tower_1 = tower_floors
    tower_2 = tower_floors
    tower_3 = tower_floors
    smillis = time.perf_counter() * 1000
    s.onkeypress(start_up, "Up")
    s.onkeypress(start_down, "Down")
    s.onkeypress(start_left, "Left")
    s.onkeypress(start_right, "Right")
    s.onkeyrelease(end_up, "Up")
    s.onkeyrelease(end_down, "Down")
    s.onkeyrelease(end_left, "Left")
    s.onkeyrelease(end_right, "Right")
    s.onkeypress(start_space, " ")
    s.onkeyrelease(end_space, " ")
    s.onclick(s.listen())
    t.addshape("plane", ( (0,-2),(1,0),(3,0),(2,1),(1,1),(0, 2),(0,1),(-1,1),(-2,3),(-2,1),(-1,0),(0,0),(0,-2)) )
    t.addshape("plane_right", ( (0,-2),(-1,0),(-3,0),(-2,1),(-1,1),(0, 2),(0,1),(1,1),(2,3),(2,1),(1,0),(0,0),(0,-2)) )
    t.addshape("bomb", ((-1,1),(1,-1),(3,-1),(4,0),(3,1),(1,1),(-1,-1)))
    t.bgcolor("black")
    t.speed(0)
    t.tracer(0, 0)
    
def main():
    global xvel, yvel, xthrust, ythrust, friction, space_pressed, state, millis, smillis, laser_x, laser_y, bomb_x, bomb_y, tower_1, tower_2, tower_3, laser_on, smillis2
    global bomb_placex, plane_x, plane_y, bomb_xvel, plane_yvel, gameover_cause, rep, tower_floors, old_space_pressed, boom1_x, boom1_y, boom2_x, boom2_y, boom1_millis
    global boom2_millis, plane_left, score, scrnsize
    scrnsize = min(t.window_width() / 700, t.window_height() / 650)
    t.ht()
    t.shapesize(round(10 * scrnsize), round(10 * scrnsize), round(4 * scrnsize))
    millis = time.perf_counter() * 1000 - smillis
    if state == "Title screen":
        t.pu()
        t.goto(0, 100)
        t.write("Bomber Takedown", align="center", font=("Courier New", round(30 * scrnsize), "bold"))
        t.goto(0, 0)
        t.write("Press space to start" * ((millis % 500) > 250), align="center", font=("Courier New", round(15 * scrnsize), "normal"))
        if not space_pressed:
            old_space_pressed = False
        if space_pressed and not old_space_pressed:
            state = "tutorial"
            xvel = 0.0
            yvel = 0.0
            laser_on = False
            plane_x = 0
            plane_y = 3001
            bomb_placex = -900
            bomb_xvel = 0
            plane_yvel = 0
            laser_x = 0
            laser_y = 0
            bomb_x = 0
            bomb_y = 3001
            tower_1 = tower_floors
            tower_2 = tower_floors
            tower_3 = tower_floors
            boom1_x = 0
            boom1_y = 0
            boom2_x = 0
            boom2_y = 0
            score = 0
            rep = 100
            old_space_pressed = True
    elif state == "tutorial":
        t.goto(0, -200)
        t.write("""
You are a gunner
controlling 3 turrets at once.
Your job here is to shoot
any bombers and bombs that they
manage to drop.
Getting a tower damaged will decrease
your reputation by 25%. If a tower falls,
it's game over. Shooting a bomb will earn
you 10% rep, while shooting a bomber will get
you 37% If your reputation reaches 0, it's
game over. Try to score as many points as
possible! Oh and just so you know, you press
the arrows to aim and space to shoot.
High scores are not saved.

Press space to continue!
""", align="center", font=("Courier New", round(15 * scrnsize), "normal"))
        if not space_pressed:
            old_space_pressed = False
        if space_pressed and not old_space_pressed:
            state = "game"
    elif state == "game":
        colliding_1 = tower(-250, -300, 75, 250, tower_floors, tower_1, colx = bomb_x, coly = bomb_y)
        colliding_2 = tower(-50, -300, 75, 280, tower_floors, tower_2, colx = bomb_x, coly = bomb_y)
        colliding_3 = tower(200, -300, 75, 250, tower_floors, tower_3, colx = bomb_x, coly = bomb_y)
        tower_1 -= int(colliding_1)
        tower_2 -= int(colliding_2)
        tower_3 -= int(colliding_3)
        xvel = xthrust + xvel
        yvel = ythrust + yvel
        xvel = xvel * friction
        yvel = yvel * friction
        laser_x = laser_x + xvel
        laser_y = laser_y + yvel
        if colliding_1 or colliding_2 or colliding_3:
            boom1_millis = millis + 500
            boom1_x = bomb_x
            boom1_y = bomb_y
            bomb_y = 3001
            rep -= 25
        if laser_on:
            if abs(bomb_x + 3000 - round(laser_x + 3000)) < collision_radius and abs(bomb_y + 3000 - round(laser_y + 3000)) < collision_radius:
                boom2_millis = millis + 500
                boom2_x = bomb_x
                boom2_y = bomb_y
                bomb_y = 3001
                rep += 10
                score += 100
            if abs(plane_x + 3000 - round(laser_x + 3000)) < collision_radius and abs(plane_y + 3000 - round(laser_y + 3000)) < collision_radius:
                boom2_millis = millis + 500
                boom2_x = plane_x
                boom2_y = plane_y
                plane_y = 3001
                rep += 37
                score += 235
        if boom1_millis < millis:
            boom1_y = 3001
        if boom2_millis < millis:
            boom2_y = 3001
        boom(boom1_x, boom1_y)
        boom(boom2_x, boom2_y)
        if bomb_y < 3000:
            bomb_xvel *= 0.97
            t.goto(bomb_x, bomb_y)
            t.seth(t.towards(bomb_x + bomb_xvel, bomb_y - 6) + 90)
            bomb_y -= 6
            bomb_x += bomb_xvel
            t.shape("bomb")
            t.stamp()
        if space_pressed and millis < (smillis2 + 100):
            laser_on = True
        elif not space_pressed:
            smillis2 = millis
            laser_on = False
        elif space_pressed:
            laser_on = False
        if(randint(0, 3) == 0):
            plane_yvel = randint(-1,1) * 3
        t.goto(plane_x, plane_y)
        t.seth((t.towards(plane_x + 9, plane_y + plane_yvel) + 90) * plane_left + (t.towards(plane_x + 9, plane_y + plane_yvel) * -1 + 90) * int(not plane_left))
        plane_x += 9 * plane_left + -9 * int(not plane_left)
        plane_y += plane_yvel
        if plane_y < 3000:
            if plane_left:
                t.shape("plane")
            else:
                t.shape("plane_right")
            t.stamp()
            if((bomb_placex < plane_x) and plane_left) or ((bomb_placex > plane_x) and not plane_left):
                bomb_placex = 900 * plane_left + -900 * int(not plane_left)
                bomb_xvel = 9 * plane_left + -9 * int(not plane_left)
                bomb_x = plane_x
                bomb_y = plane_y
        if abs(plane_x) > 400:
            plane_left = bool(randint(0,1))
            plane_x = -400 * plane_left + 400 * int(not plane_left)
            plane_y = randint(100, 250)
            bomb_placex = randint(-400, randint(-400, 400)) * plane_left + randint(randint(-400, 400), 400) * int(not plane_left)
        t.goto(laser_x, laser_y)
        t.dot(round(12 * scrnsize), "red")
        t.goto(-340, 300)
        t.write("{}% reputation".format(rep), align="left", font=("Courier New", round(12 * scrnsize), "normal"))
        t.goto(340, 300)
        t.write("{} score".format(score), align="right", font=("Courier New", round(12 * scrnsize), "normal"))
        if rep > 100:
            rep = 100
        if rep < 0:
            rep = 0
        if rep == 0:
            gameover_cause = "Your reputation died."
            state = "gameover"
        if tower_1 == 0 or tower_2 == 0 or tower_3 == 0:
            gameover_cause = "One of your towers fell."
            state = "gameover"
    elif state == "gameover":
        t.goto(0, 100)
        t.write("Game over!", align="center", font=("Courier New", round(30 * scrnsize), "normal"))
        t.goto(0,0)
        t.write("Score: {}".format(score), align="center", font=("Courier New", round(12 * scrnsize), "normal"))
        t.goto(0, -100)
        t.write(gameover_cause, align="center", font=("Courier New", round(13 * scrnsize), "normal"))
        t.goto(0, -120)
        t.write("Press space to retry", align="center", font=("Courier New", round(13 * scrnsize), "normal"))
        if space_pressed:
            state = "Title screen"
            old_space_pressed = True

print("Functions declared")
#if __name__ == "__main__":
def drawwindowsize(w=int, h=int):
    t.setworldcoordinates(w / -2, h / -2, w / 2, h / 2)
init()
print("Initialization function finished. Starting main loop...")
while True:
    if((t.window_width() - 50) > t.window_height()):
        drawwindowsize(700 * t.window_width() / 700 * 650 / t.window_height(), 650)
        
    else:
        drawwindowsize(700, 650 * t.window_height() / 650 * 700 / t.window_width())
    t.clear()
    t.color("white")
    t.begin_fill()
    t.goto(-700 / 2, -650 / 2)
    t.goto(-700 / 2, 650 / 2)
    t.goto(700 / 2, 650 / 2)
    t.goto(700 / 2, -650 / 2)
    t.goto(-700 / 2, -650 / 2)
    t.end_fill()
    t.color("black")
    main()
    time.sleep(0.01)
    t.update()
