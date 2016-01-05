# Crappy Bird

## Design Specification

Tools and Framework

I used http://runpython.com to write this program. I imported ggame, and from that I imported App, Color, LineStyle, Sprite, ImageAsset, and Frame.

Language

I used Python 3

Elements, Logic, and Code

There are many elements to my project, and they all need code to support them and get them to execute what they need to do. I did those using classes and step functions. First, the bird. I made a class for the bird with all the qualities I wanted it to have. I also wrote a step function that responds to the space bar being pressed. Each time it is pressed, the bird goes up 30 pixels. Next, the walls. For the walls, I had them have random y values each time they are spawned and a starting x value of 400, the right edge of the screen. Each frame, it moves 3 pixels to the left. When the x value is -100, it resets to 400 to create infinite walls. Collisions with walls, coded in the birds class function, result in a game over.

Data Storage and Manipulation

My program does not store or manipulate data. It simply runs the code necessary for the game to be played. In future versions I might add a feature that stores the highest score, but for now I am sticking to the basics.

Unusual or Notable Algorithms

One algorithm that I used was to create the idea of gravity. As you know if you have ever dropped a rock off a high place, the rate of falling is not constant. I incorporated this into my code with gravity and acceleration. The base acceleration starts at falling .5 pixels per frame. Each time the frame is called, this value increases by .1. This ends up with a display that when falling, the bird seems to go faster the longer it falls. Also, the acceleration is reset to .5 each time the spacebar is pressed and the bird jumps, to prevent infinitely growing acceleration.
