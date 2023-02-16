import random


class Point:

    def __init__(self, x, y, old_x, old_y):
        self.x = x
        self.y = y
        self.old_x = old_x
        self.old_y = old_y

        self.rect = None
        self.fixed = False


class Stick:

    def __init__(self, p0, p1):
        self.p0 = p0
        self.p1 = p1
        self.length = self.distance()
        self.rect = None

    def distance(self):
        dx = self.p1.x - self.p0.x
        dy = self.p1.y - self.p0.y
        return (dx**2 + dy**2)**0.5
