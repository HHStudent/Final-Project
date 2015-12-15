"""
Name: Dimitri Somoff
Final Project: Flappy bird remake "Crappy Bird"
"""
from ggame import App, Color, LineStyle, Sprite, ImageAsset, Frame

class Bird(Sprite):
    asset1 = ImageAsset("images/0.png")
    asset2 = ImageAsset("images/1.png")
    asset3 = ImageAsset("images/2.png")
    
    def __init__(self, position):
        super().__init__(Bird.asset1, position)
        self.birdy = 350
        CrappyApp.listenKeyEvent("keydown", "space", self.Jump)
        
    def Jump(self, event):
        self.birdy += 5


class CrappyApp(App):
    def __init__(self, width, height):
        super().__init__(width, height)
        bg_asset = ImageAsset("images/background.png")
        bg = Sprite(bg_asset, (0,0))
        Bird((0, 350))
        




myapp = CrappyApp(400, 708)
myapp.run()