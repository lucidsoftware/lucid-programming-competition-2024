import heapq

(w, l, k) = [int(x) for x in input().split()]
grid = []

for i in range(l):
    grid.append([[int(x) for x in coorStr.split(',')] for coorStr in input().split()])

queue = []
for i in range(len(grid[0])):
    # the queue will sort based upon these values in order
    # negated downward velocity, negated y position, sailsDown, time taken, toggle cooldown, x velocity, x position
    heapq.heappush(queue, (1, -1, -0, False, 0,  0, i))

while len(queue) > 0:
    (time, negatedYVelocity, negatedYPosition, sailsDown, cooldown, xVelocity, xPosition) = heapq.heappop(queue)
    yVelocity = -negatedYVelocity
    yPosition = -negatedYPosition
    if yPosition >= l:
        print(time)
        break
    newYVelocity = yVelocity + grid[yPosition][xPosition][1]
    newXVelocity = xVelocity + grid[yPosition][xPosition][0]
    sailsUpCooldown = 0
    sailsDownCooldown = 0
    if sailsDown and cooldown == 0:
        sailsUpCooldown = k - 1
    elif not sailsDown and cooldown == 0:
        sailsDownCooldown = k - 1
    elif cooldown != 0:
        sailsUpCooldown = cooldown - 1
        sailsDownCooldown = cooldown - 1

    sailsUpXPosition = xPosition + newXVelocity
    sailsUpYPosition = yPosition + newYVelocity
    sailsDownXPosition = xPosition + xVelocity
    sailsDownYPosition = yPosition + yVelocity

    sailsUpTuple = (time + 1, -newYVelocity, -sailsUpYPosition, False, sailsUpCooldown, newXVelocity, sailsUpXPosition)
    sailsDownTuple = (time + 1, -yVelocity, -sailsDownYPosition, True, sailsDownCooldown, xVelocity, sailsDownXPosition)

    if cooldown == 0:
        if sailsUpXPosition >= 0 and sailsUpXPosition < w:
            heapq.heappush(queue, sailsUpTuple)
        if sailsDownXPosition >= 0 and sailsDownXPosition < w:
            heapq.heappush(queue, sailsDownTuple)
    elif sailsDown:
        if sailsDownXPosition >= 0 and sailsDownXPosition < w:
            heapq.heappush(queue, sailsDownTuple)
    else:
        if sailsUpXPosition >= 0 and sailsUpXPosition < w:
            heapq.heappush(queue, sailsUpTuple)