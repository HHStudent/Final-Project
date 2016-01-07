"""
Name: Dimitri Somoff
Final Project: Flappy bird remake "Crappy Bird"
"""
from ggame import App, Color, LineStyle, Sprite, ImageAsset, Frame, SoundAsset
import random

wals = 0
bottomwals = 0
globvar = 0
scorevar = 0

def set_globvar_to_one():
    global globvar
    globvar = 1

def add_score_var():
    global scorevar
    scorevar += 1

class TopWall(Sprite):
    top = ImageAsset("images/top.png")
    def __init__(self, position):
        super().__init__(TopWall.top, position)

    def step(self):
        if self.x <= -100 and self.y == -201:
            self.y = -420
            self.x = 400
            add_score_var()
        elif self.x <= -100 and self.y == -420:
            self.y = -25
            self.x = 400
            add_score_var()
        elif self.x <= -100 and self.y == -25:
            self.y = -290
            self.x = 400
            add_score_var()
        elif self.x <= -100 and self.y == -290:
            self.y = -135
            self.x = 400
            add_score_var()
        elif self.x <= -100 and self.y == -135:
            self.y = -400
            self.x = 400
            add_score_var()
        elif self.x <= -100 and self.y == -400:
            self.y = -200
            self.x = 400
            add_score_var()
        elif self.x <= -100 and self.y == -200:
            self.y = -420
            self.x = 400
            add_score_var()
        if self.visible == True:
            collides = self.collidingWithSprites(DeadBird)
            if len(collides):
                self.x = 30
                set_globvar_to_one()
            else:
                self.x -= 3
        if globvar == 1:
            self.x = 30

class BottomWall(Sprite):
    bottom = ImageAsset("images/bottom.png")
    def __init__(self, position):
        super().__init__(BottomWall.bottom, position)
        self.iswalls = True
        
    def step(self):
        if self.x <= -100 and self.y == 424:
            self.y = 205
            self.x = 400
        elif self.x <= -100 and self.y == 205:
            self.y = 600
            self.x = 400
        elif self.x <= -100 and self.y == 600:
            self.y = 335
            self.x = 400
        elif self.x <= -100 and self.y == 335:
            self.y = 490
            self.x = 400
        elif self.x <= -100 and self.y == 490:
            self.y = 225
            self.x = 400
        elif self.x <= -100 and self.y == 225:
            self.y = 425
            self.x = 400
        elif self.x <= -100 and self.y == 425:
            self.y = 205
            self.x = 400
        if self.visible == True:
            collides = self.collidingWithSprites(DeadBird)
            if len(collides):
                self.x = 30
                set_globvar_to_one()
            else:
                self.x -= 3
        if globvar == 1:
            self.x = 30

class Bird(Sprite):
    asset1 = ImageAsset("images/0.png")
    asset2 = ImageAsset("images/1.png")
    asset3 = ImageAsset("images/2.png")
    
    def __init__(self, position):
        super().__init__(Bird.asset1, position)
        self.birdy = 350
        self.gravity = .1
        self.wallx = 400
        self.wally = random.randint(-420, 0)
        self.bottomwally = self.wally + 625
        CrappyApp.listenKeyEvent("keydown", "space", self.Jump)

    def step(self):
        self.gravity += .15
        self.birdy += self.gravity
        self.y = self.birdy
        self.spawnwalls()
        self.wallx -= 3
        if self.visible == True:
            collides = self.collidingWithSprites(TopWall)
            collides1 = self.collidingWithSprites(BottomWall)
            if len(collides):
                self.die()
            if len(collides1):
                self.die()
        if self.visible == True:
            if self.y <= 10 or self.y >= 665:
                self.die()

    def Jump(self, event):
        self.birdy -= 50
        self.gravity = .1

    def spawnwalls(self):
        if self.wallx == 400:
            TopWall((self.wallx, -201))
            BottomWall((self.wallx, 424))

    def die(self):
        self.visible = False
        DeadBird((self.x, self.y))
        self.destroy()
        print("Your score was {0}!".format(scorevar))
        if scorevar < 1:
            #print("Wow, you are really bad. Actually, have you ever accomplished anything before?")
            print("Hint: press the space bar to fly!")
        elif scorevar < 2:
            #print("Are you even trying? I seriously hope this is a joke and you aren't this incompetent.")
            print("Nice one! Try again!")
        elif scorevar < 5:
            #print("I guess you aren't terrible. Still, try harder for once.")
            print("Awesome! You are really getting the hang of this!")
        elif scorevar < 10:
            #print("Wow, you got a halfway decent score. I'm sure your parents are proud.")
            print("You are amazing!")
        elif scorevar < 20:
            #print("Finally, a double digit score. I didn't know you had it in you.")
            print("Very impressive! You are a pro.")
        else:
            #print("Tryhard. Go do something worthwhile with your life.")
            print("You are the best at this game!")

class DeadBird(Sprite):
    
    asset = ImageAsset("images/dead.png")

    def __init__(self, position):
        super().__init__(DeadBird.asset, position)

class CrappyApp(App):
    def __init__(self, width, height):
        super().__init__(width, height)
        bg_asset = ImageAsset("images/background.png")
        bg = Sprite(bg_asset, (0,0))
        Bird((20, 350))

    def step(self):
        for bird in self.getSpritesbyClass(Bird):
            bird.step()
        for birds in self.getSpritesbyClass(TopWall):
            birds.step()
        for bottoms in self.getSpritesbyClass(BottomWall):
            bottoms.step()

myapp = CrappyApp(400, 708)
myapp.run()