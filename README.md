# square-chaos-game
Square chaos game made in python using Pygame

First attempt with Pygame, and I am pretty new at vim, so if the code is ugly thats because I
was lazy

The argument is that the `last chosen vertex + argument` cannot be chosen again. If we consider
four vertices, `[0,1,2,3]`, and, if the last chosen was `X`, the next chosen vertice cannot be the
`(X + argument) % 4`.

Look up the wikipedia for Chaos Game, or the Numberphile video (altough they do in triangles,
but is the same principle): they can explain better than me.

This was based in the The Coding Train(https://www.youtube.com/watch?v=7gNzMtYo9n4) video.
