"# Define the base class player
class player:
    def play(self):
        print("The player is playing cricket.")

# Define the derived class batsman
class batsman(player):
    def play(self):
        print("The batsman is batting.")

# Define the derived class bowler
class bowler(player):
    def play(self):
        print("The bowler is bowling.")

# Create objects of batsman and bowler classes
batsman = batsman()
bowler = bowler()

#call the play() method for each object
batsman.play()
bowler.play()""
This is the Template Repl for Python with Turtle.

Python with Turtle lets you make graphics easily in Python.

Check out the official docs here: https://docs.python.org/3/library/turtle.html
"""

import turtle

t = turtle.Turtle()

for c in ['red', 'green', 'blue', 'yellow']:
    t.color(c)
    t.forward(75)
    t.left(90)