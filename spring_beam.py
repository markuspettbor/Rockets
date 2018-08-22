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
    '''startpos should contain the position for the two nodes connected to the spring
    the order they are given is important, they are returned in the same order'''
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
        self.l0 = sum((self.pos[1]-self.pos[0])**2)**.5

    def getStiffness(self):
        return self.stiffness

    def getFracture(self):
        return self.fracture

    def getPos(self):
        return self.pos

    def setPos(self, movement):
        try:
            self.pos = self.pos + movement
        except ValueError:
            print('self.pos and movement are different sizes/shapes, movement should be [[x1,y1],[x2,y2]]')

    def getForce(self): # Hooke sier:
        pos = self.pos
        '''centre = (pos[0] + pos[1])/2
        direction1 = pos[0] - centre
        direction2 = pos[1] - centre
        simplified-->'''
        dir1 = (pos[0]-pos[1])/2
        dir2 = (pos[1]-pos[0])/2
        length = sum((pos[1]-pos[0])**2)**.5
        force = self.stiffness * (self.l0 - length)
        return (dir1*force, dir2*force) #returns force for node 1 and node 2
'''
n1 = Node(1, [1,1])
mass = n1.getMass()
print(mass)
npos = n1.getPos()
print(npos)
n1.setPos([-0.1,0.1])
npos = n1.getPos()
print(npos)
n1.setPos([-0.1,0.1])
npos = n1.getPos()
print(npos)
n1.setPos([-0.1,0.1])
npos = n1.getPos()
print(npos)
weigth = n1.getWeigth()
print(weigth)
'''
'''
s1 = Spring(0.2,4,[[0,0],[1,1]])
stiff = s1.getStiffness()
print(stiff)
frac = s1.getFracture()
print(frac)
pos = s1.getPos()
print(pos)
force1, force2 = s1.getForce()
print(force1, force2)
s1.setPos([[-1,-1],[1,1]])
pos = s1.getPos()
print(pos)
force1, force2 = s1.getForce()
print(force1, force2)
'''
