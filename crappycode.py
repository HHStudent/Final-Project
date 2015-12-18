"""
Name: Dimitri Somoff
Final Project: Flappy bird remake "Crappy Bird"
"""
from ggame import App, Color, LineStyle, Sprite, ImageAsset, Frame
import random

wals = 0

class TopWall(Sprite):
    top = ImageAsset("images/top.png")
    def __init__(self, position):
        super().__init__(TopWall.top, position)
        
    def step(self):
        if self.x <= -30:
            wals = random.randint(-420, 0)
            bottomwals = wals + 625
            self.y = wals
            self.x = 400
        self.x -= 3

class BottomWall(Sprite):
    bottom = ImageAsset("images/bottom.png")
    def __init__(self, position):
        super().__init__(BottomWall.bottom, position)
        
    def step(self):
        if self.x <= -30:
            self.y = bottomwals
            self.x = 400
        self.x -= 3

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
        #if self.wallx <= 0:
        #    self.wallx = 400
        self.spawnwalls()
        self.wallx -= 3

    def Jump(self, event):
        self.birdy -= 50
        self.gravity = .1

    def spawnwalls(self):
        if self.wallx == 400:
            self.wally = random.randint(-420, 0)
            self.bottomwally = self.wally + 625
            TopWall((self.wallx, self.wally))
            BottomWall((self.wallx, self.bottomwally))
        

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