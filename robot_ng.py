from robot import Robot
from point import Point
from operator import attrgetter
import math


class RobotNG(Robot):
    nom = "Robot nouvelle génération"
    version = 1

    def __init__(self, x, y, orientation):
        super().__init__(x, y, orientation)

    def avancer(self, npas):
        i = 0
        while i < npas:
            super().avance()
            i = i + 1

    def tourner_gauche(self):
        self.orientation = (self.orientation + 3) % 4

    def demi_tour(self):
        self.orientation = (self.orientation + 2) % 4

    def distance(self, point2):
        dist = math.sqrt(
            (point2.x - self.position.x) * (point2.x - self.position.x)
            + (point2.y - self.position.y) * (point2.y - self.position.y)
        )
        # print("La distance est : {}".format(dist))
        return dist

    def next_step(self, chemin):
        # list des distance
        nextStepIndex = 0
        nextStepDist = 0
        i = 0
        while i < len(chemin):
            distance = 0
            point = chemin[i]
            distance = self.distance(point)
            if i == 0:
                nextStepDist = distance
            elif i > 0 and distance < nextStepDist:
                nextStepDist = distance
                nextStepIndex = i
            i = i + 1
        self.position = chemin[nextStepIndex]
        chemin.pop(nextStepIndex)
        print("next Poition: ", self.position)
        return self.position

    def trajet(self, chemin):
        # clone chemin
        clonedList = chemin[:]
        len(clonedList)
        while len(clonedList) > 0:
            point = self.next_step(clonedList)
            index = next(
                (
                    i
                    for i, item in enumerate(chemin)
                    if item.x == point.x and item.y == point.y
                ),
                -1,
            )
            print("p", index)
