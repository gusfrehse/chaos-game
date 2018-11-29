#!/usr/bin/env python3
import sys, pygame, random, math
pygame.init()

size = width, height = 1280, 720
white = 255,255,255
black = 0, 0, 0
screen = pygame.display.set_mode(size)
check = 0
numberOfPoints = 3 
checkIfSame = False

# Check for input
print(sys.argv)
if len(sys.argv) >= 2: 
    numberOfPoints = int(sys.argv[1])
if len(sys.argv) >= 3:
    if (sys.argv[2] == "true"):
        checkIfSame = True
    elif (sys.argv[2] == "false"):
        checkIfSame = False
    else:
        print("The 2nd argument must be 'true' or 'false'")
if len(sys.argv) >= 4:
    check = int(sys.argv[3])

# Easier to understand
def drawPoint(xandy, color):
    pygame.draw.rect(screen, color, (int(xandy[0] - 0.5), int(xandy[1] - 0.5), 1, 1)) 

# Define the points
angle = math.tau / numberOfPoints
points = []
scale = (min(width, height) - 2) / 2
for i in range(numberOfPoints):
    points.append([width/2 + scale * math.sin((i * angle) + math.pi), height/2 + scale * math.cos((i * angle) + math.pi)])

pointNew = [width/2, height/2]
divisor = 2
lastWhichPoint = -1

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    # Do hundred times a frame so it is faster to see the fractal
    for i in range(100):
        # Random point check if the last vertex + the input is the chosen
        whichPoint = random.randint(0, numberOfPoints - 1)
        while checkIfSame and whichPoint == (lastWhichPoint + check) % numberOfPoints:
            whichPoint = random.randint(0, numberOfPoints - 1)
        # Move one point in the direction of the chosen point
        for index,point in enumerate(points):
            if whichPoint == index:
                # Lerp
                pointNew = [pointNew[0] + (point[0] - pointNew[0])/divisor, pointNew[1] + (point[1] - pointNew[1])/divisor]
    
        lastWhichPoint = whichPoint
    
        # Rendering
        for point in points:
            drawPoint(point, (255, 0, 0, 0.5))
        drawPoint(pointNew, (0, 255, 0))

    pygame.display.flip()
