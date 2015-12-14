"""
Name: Dimitri Somoff
Final Project: Flappy bird remake "Crappy Bird"
"""
from ggame import App, Color, LineStyle, Sprite, ImageAsset, Frame

"""class CrappyBird(Sprite):
    
    def __init__(self, x, y):
        super().__init__(x, y)
        
"""

class CrappyApp(App):
    background = ImageAsset("images/background.png")
    
    def __init__(self, width, height):
        super().__init__(width, height)
        bg = Sprite(background, (0,0))
        




myapp = CrappyApp(400, 708)
myapp.run()