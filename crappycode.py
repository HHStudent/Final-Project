"""
Name: Dimitri Somoff
Final Project: Flappy bird remake "Crappy Bird"
"""
from ggame import App, Color, LineStyle, Sprite, ImageAsset, Frame

class Bird(Sprite):
    images = [((ImageAsset("images/0.png")), (ImageAsset("images/1.png")), (ImageAsset("images/2.png")))]
    asset1 = ImageAsset("images/0.png")
    asset2 = ImageAsset("images/1.png")
    asset3 = ImageAsset("images/2.png")
    
    def __init__(self, position):
        super().__init__(Bird.images[0], position)
        self.birdy = 350
        CrappyApp.listenKeyEvent("keydown", "space", self.Jump)

    def step(self):
        self.y = self.birdy

    def Jump(self, event):
        self.birdy -= 5
        self.SetImage(Bird.asset2)


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