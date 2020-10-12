import random

def oneDimWalk():
    pos = 0
    crossedStart = 0
    for i in range(0, 10000):
        pos += random.randint(-1, 1)
        if pos == 0:
            crossedStart += 1
    return crossedStart

def twoDimWalk():
    posX = 0
    posY = 0
    crossedStart = 0
    for i in range(0, 100000):
        posX += random.randint(-1, 1)
        posY += random.randint(-1, 1)
        if posX == 0 and posY == 0:
            crossedStart += 1
    return crossedStart

def threeDimWalk():
    posX = 0
    posY = 0
    posZ = 0
    crossedStart = 0
    for i in range(0, 100000):
        posX += random.randint(-1, 1)
        posY += random.randint(-1, 1)
        posZ += random.randint(-1, 1)
        if posX == 0 and posY == 0 and posZ == 0:
            crossedStart += 1
    return crossedStart

crossed1 = 0
for i in range(0, 100):
    if oneDimWalk() > 0:
        crossed1 += 1
print("In 100 random 1D walks of length 10,000, " + str(crossed1) + " returned to the origin at least once.")

crossed2 = 0
for i in range(0, 100):
    if twoDimWalk() > 0:
        crossed2 += 1
print("In 100 random 2D walks of length 100,000, " + str(crossed2) + " returned to the origin at least once.")

crossed3 = 0
for i in range(0, 100):
    if threeDimWalk() > 0:
        crossed3 += 1
print("In 1000 random 3D walks of length 100,000, " + str(crossed3) + " returned to the origin at least once.")
