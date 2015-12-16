"""
Name: Dimitri Somoff
Final Project: Flappy bird remake "Crappy Bird"
"""
from ggame import App, Color, LineStyle, Sprite, ImageAsset, Frame
import random

class TopWall(Sprite):
    top = ImageAsset("images/top.png")
    def __init__(self, position):
        super().__init__(TopWall.top, position)
        
    def step(self):
        self.x -= 5
        
class BottomWall(Sprite):
    bottom = ImageAsset("images/bottom.png")
    def __init__(self, position):
        super().__init__(BottomWall.bottom, position)
        
    def step(self):
        self.wallx -= 5

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
        self.gravity += .05
        self.birdy += self.gravity
        self.y = self.birdy
        self.spawnwalls()
        #for tops in self.getSpritesbyClass(TopWall):
        #    tops.step()
        #for bottoms in self.getSpritesbyClass(BottomWall):
        #    bottoms.step()
        #TopWall((self.wallx, self.wally))
        #self.wallx -= 5

    def Jump(self, event):
        self.birdy -= 20
        self.gravity = .1

    def spawnwalls(self):
        if self.wallx == 400:
            TopWall((self.wallx, self.wally))
            BottomWall((self.wallx, self.bottomwally))
            self.wallx -= 5
        #elif self.wallx == 300:
         #   self.wallx == 400
         #   TopWall((self.wallx, self.wally))
            #BottomWall((self.wallx, self.bottomwally))
        else:
            self.wallx -= 5


    

class CrappyApp(App):
    def __init__(self, width, height):
        super().__init__(width, height)
        bg_asset = ImageAsset("images/background.png")
        bg = Sprite(bg_asset, (0,0))
        Bird((20, 350))
        

    def step(self):
        for bird in self.getSpritesbyClass(Bird):
            bird.step()
        for tops in self.getSpritesbyClass(TopWall):
            tops.step()
        

myapp = CrappyApp(400, 708)
myapp.run()