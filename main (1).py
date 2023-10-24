# leap year
def isleapyear(year):
   if(year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
     return True
   else:
     return False

year = int(input("Enter a year :"))

if isleapyear(year):
  print('{} is a leap year.'.format(year))
else:
  print('{} is not a leap year.'.format(year))"""
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