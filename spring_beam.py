import numpy as np

class Node(object):
    def __init__(self, mass, startpos, radius = 0):
        try:
            self.mass = float(mass)
            self.radius = float(radius)
        except TypeError:
            print('Node object was given invalid number(s)')
        try:
            self.pos = np.array(startpos)
        except TypeError:
            print('Node startposition could not be converted to np.array')

    def getMass(self):
        return self.mass

    def getRadius(self):
        return self.radius

    def getWeigth(self, grav = 9.81): #in newtons [N]
        return self.mass * grav

    def getPos(self):
        return self.pos

    def setPos(self, movement):
        movement = np.array(movement)
        self.pos = self.pos + movement

class Spring(object):
    def __init__(self, stiffness, fracture, startpos):
        try:
            self.stiffness = float(stiffness)
            self.fracture = float(fracture)
        except TypeError:
            print('Spring object was given invalid number(s)')
        try:
            self.pos = np.array(startpos)
        except TypeError:
            print('Startposition could not be converted to np.array')

    def getStiffness(self):
        return self.stiffness

    def getFracture(self):
        return self.fracture

    def getPos(self):
        return (pos)

    def setPos(self, movement):
        try:
            self.pos = self.pos + movement
        except ValueError:
            print('self.pos and movement are different sizes/shapes, movement should be [[x1,y1],[x2,y2]]')

    def getForce(self): # Hooke says:
        centre = (self.pos[0] + self.pos[1])/2
        force1 =

n1 = Node(1)
