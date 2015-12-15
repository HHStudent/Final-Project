"""
Name: Dimitri Somoff
Final Project: Flappy bird remake "Crappy Bird"
"""
from ggame import App, Color, LineStyle, Sprite, ImageAsset, Frame
import random

class Bird(Sprite):
    asset1 = ImageAsset("images/0.png")
    asset2 = ImageAsset("images/1.png")
    asset3 = ImageAsset("images/2.png")
    
    def __init__(self, position):
        super().__init__(Bird.asset1, position)
        self.birdy = 350
        self.gravity = .1
        self.wallx = 400
        self.wally = random.randint(-400, 0)
        self.bottomwally = self.wally - 130
        CrappyApp.listenKeyEvent("keydown", "space", self.Jump)

    def step(self):
        self.gravity += .05
        self.birdy += self.gravity
        self.y = self.birdy
        TopWall((self.wallx, self.wally))
        BottomWall((self.wallx, self.bottomwally))
        self.wallx -= 10

    def Jump(self, event):
        self.birdy -= 20
        self.gravity = .1

class TopWall(Sprite):
    top = ImageAsset("images/top.png")
    
    def __init__(self, position):
        super().__init__(TopWall.top, position)
        
class BottomWall(TopWall):
    bottom = ImageAsset("images/bottom.png")
    
    def __init__(self, position):
        super().__init__(BottomWall.bottom, position)
        self.y = y + 130
    

class CrappyApp(App):
    def __init__(self, width, height):
        super().__init__(width, height)
        bg_asset = ImageAsset("images/background.png")
        bg = Sprite(bg_asset, (0,0))
        Bird((20, 350))
        

    def step(self):
        for bird in self.getSpritesbyClass(Bird):
            bird.step()
        




myapp = CrappyApp(400, 708)
myapp.run()