# Factorial
def fact_rec(n):
  if n==0 or n==1:
     return 1
  else:
     return n*fact_rec(n-1)
number = int(input("Enter a value :"))
res = fact_rec(number)

print("The factorial of {} is {} .". format (number,res))"""
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