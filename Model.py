import numpy as np
import math

class Engine:

    def __init__(self):

        self.actualPlayer = 1
        self.winner = 0
        self.dataMatrix = np.zeros((3, 3, 3))

    def step(self, x, y, z):

        if self.dataMatrix[x, y, z] == 0:
            self.dataMatrix[x, y, z] = self.actualPlayer

            if self.actualPlayer == 1:
                self.actualPlayer = 2
            else:
                self.actualPlayer = 1
            winner = self.findWinner()
            if winner != 0:
                self.winner = winner
            if self.isFull() and winner == 0:
                self.winner = 3


    def checkCols(self):
        for z in range(3):
            for x in range(3):
                if (self.dataMatrix[x, 0, z] != 0) and (self.dataMatrix[x, 0, z] == self.dataMatrix[x, 1, z] == self.dataMatrix[x, 2, z]):
                    return self.dataMatrix[x, 0, z]
        return 0

    def checkRows(self):
        for z in range(3):
            for y in range(3):
                if (self.dataMatrix[0, y, z] != 0) and (self.dataMatrix[0, y, z] == self.dataMatrix[1, y, z] == self.dataMatrix[2, y, z]):
                    return self.dataMatrix[0, y, z]
        for x in range(3):
            for y in range(3):
                if (self.dataMatrix[x, y, 0] != 0) and (self.dataMatrix[x, y, 0] == self.dataMatrix[x, y, 1] == self.dataMatrix[x, y, 2]):
                    return self.dataMatrix[x, y, 0]
        return 0

    def checkDiags(self):

        for z in range(3):
            if (self.dataMatrix[0, 0, z] != 0) and (self.dataMatrix[0, 0, z] == self.dataMatrix[1, 1, z] == self.dataMatrix[2, 2, z]):
                return self.dataMatrix[0, 0, z]
            if (self.dataMatrix[0, 2, z] != 0) and (self.dataMatrix[0, 2, z] == self.dataMatrix[1, 1, z] == self.dataMatrix[2, 0, z]):
                return self.dataMatrix[0, 2, z]

        for x in range(3):
            if (self.dataMatrix[x, 0, 0] != 0) and (self.dataMatrix[x, 0, 0] == self.dataMatrix[x, 1, 1] == self.dataMatrix[x, 2, 2]):
                return self.dataMatrix[x, 0, 0]
            if (self.dataMatrix[x, 2, 0] != 0) and (self.dataMatrix[x, 2, 0] == self.dataMatrix[x, 1, 1] == self.dataMatrix[x, 0, 2]):
                return self.dataMatrix[x, 2, 0]

        for y in range(3):
            if (self.dataMatrix[0, y, 0] != 0) and (self.dataMatrix[0, y, 0] == self.dataMatrix[1, y, 1] == self.dataMatrix[2, y, 2]):
                return self.dataMatrix[0, y, 0]
            if (self.dataMatrix[2, y, 0] != 0) and (self.dataMatrix[2, y, 0] == self.dataMatrix[1, y, 1] == self.dataMatrix[0, y, 2]):
                return self.dataMatrix[2, y, 0]

        return 0

    def checkBodyDiags(self):

        if (self.dataMatrix[0, 0, 0] != 0) and (self.dataMatrix[0, 0, 0] == self.dataMatrix[1, 1, 1] == self.dataMatrix[2, 2, 2]):
            return self.dataMatrix[0, 0, 0]
        if (self.dataMatrix[2, 0, 0] != 0) and (self.dataMatrix[2, 0, 0] == self.dataMatrix[1, 1, 1] == self.dataMatrix[0, 2, 2]):
            return self.dataMatrix[2, 0, 0]
        if (self.dataMatrix[2, 2, 0] != 0) and (self.dataMatrix[2, 2, 0] == self.dataMatrix[1, 1, 1] == self.dataMatrix[0, 0, 2]):
            return self.dataMatrix[2, 2, 0]
        if (self.dataMatrix[0, 2, 0] != 0) and (self.dataMatrix[0, 2, 0] == self.dataMatrix[1, 1, 1] == self.dataMatrix[2, 0, 2]):
            return self.dataMatrix[0, 2, 0]
        return 0

    def getDataMatrix(self):
        return self.dataMatrix

    def getActualPlayer(self):
        return self.actualPlayer

    def findWinner(self):
        winner = self.checkCols()
        if winner != 0:
            return winner
        winner = self.checkRows()
        if winner != 0:
            return winner
        winner = self.checkDiags()
        if winner != 0:
            return winner
        winner = self.checkBodyDiags()
        if winner != 0:
            return winner
        return 0

    def isFull(self):

        for x in range(3):
            for y in range(3):
                for z in range(3):
                    if self.dataMatrix[x, y, z] == 0:
                        return False
        return True

class Point:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def pos(self):
        return (self.x, self.y, self.z)

    def add(self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z

    def addCoord(self, modList):
        self.x += modList[0]
        self.y += modList[1]

    def rotateYaxis(self, origo, deg):
        transX = self.x - origo.x
        transZ = self.z - origo.z
        rad = math.radians(deg)

        self.x = transX * math.cos(rad) - transZ * math.sin(rad) + origo.x
        self.z = transX * math.sin(rad) + transZ * math.cos(rad) + origo.z

    def rotateXaxis(self, origo, deg):
        transZ = self.z - origo.z
        transY = self.y - origo.y
        rad = math.radians(deg)

        self.z = transZ * math.cos(rad) - transY * math.sin(rad) + origo.z
        self.y = transZ * math.sin(rad) + transY * math.cos(rad) + origo.y

    def rotateZaxis(self, origo, deg):
        transX = self.x - origo.x
        transY = self.y - origo.y
        rad = math.radians(deg)

        self.x = transX * math.cos(rad) - transY * math.sin(rad) + origo.x
        self.y = transX * math.sin(rad) + transY * math.cos(rad) + origo.y

    def equals(self, other):
        return self.x == other.x and self.y == other.y

    def project(self):
        d = 200

        return (self.x * (d / self.z) + 360, self.y * (d / self.z) + 360)

    def getZ(self):
        return self.z
