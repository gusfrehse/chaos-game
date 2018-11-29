# square-chaos-game
Square chaos game made in python using Pygame

First attempt with Pygame, and I am pretty new at vim, so if the code is ugly thats because I
was lazy.

Look up the wikipedia for Chaos Game, or the Numberphile video (altough they do in triangles,
but is the same principle): they can explain better than me.

This was based in the The Coding Train video (https://www.youtube.com/watch?v=7gNzMtYo9n4).


# Input
This is how to start the program

`./main.py [SIDES] [CHECK] [VERTEX]`

Where:
* `SIDES` is the number of sides or vertices
* `CHECK` is a boolean (`true` or `false`) that determines whether the application should check if the current chosen vertex is equal to another specific vertex (defaulted to the previously chosen vertex)
* `VERTEX` is an integer that determines how many places away from the previously chosen vertex the current vertex cannot be.
