import pygame
from Model import Point

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GRAY = (100, 100, 100)

pygame.init()
window = pygame.display.set_mode((720, 720))
pygame.display.set_caption("3D Tick Tack Toe")

class Cube:

    def __init__(self, x, y, z, size):

        self.center = Point(x, y, z)

        r = size/2

        self.A = Point(x-r, y-r, z-r)
        self.B = Point(x+r, y-r, z-r)
        self.C = Point(x-r, y+r, z-r)
        self.D = Point(x+r, y+r, z-r)
        self.E = Point(x-r, y-r, z+r)
        self.F = Point(x+r, y-r, z+r)
        self.G = Point(x-r, y+r, z+r)
        self.H = Point(x+r, x+r, z+r)

    def draw(self, win):

        pygame.draw.line(win, BLACK, self.A.project(), self.B.project(), 1)
        pygame.draw.line(win, BLACK, self.A.project(), self.C.project(), 1)
        pygame.draw.line(win, BLACK, self.C.project(), self.D.project(), 1)
        pygame.draw.line(win, BLACK, self.B.project(), self.D.project(), 1)

        pygame.draw.line(win, BLACK, self.A.project(), self.E.project(), 1)
        pygame.draw.line(win, BLACK, self.C.project(), self.G.project(), 1)
        pygame.draw.line(win, BLACK, self.D.project(), self.H.project(), 1)
        pygame.draw.line(win, BLACK, self.B.project(), self.F.project(), 1)

        pygame.draw.line(win, BLACK, self.G.project(), self.H.project(), 1)
        pygame.draw.line(win, BLACK, self.G.project(), self.E.project(), 1)
        pygame.draw.line(win, BLACK, self.F.project(), self.H.project(), 1)
        pygame.draw.line(win, BLACK, self.F.project(), self.E.project(), 1)

    def rotateY(self, deg):

        self.A.rotateYaxis(self.center, deg)
        self.B.rotateYaxis(self.center, deg)
        self.C.rotateYaxis(self.center, deg)
        self.D.rotateYaxis(self.center, deg)
        self.E.rotateYaxis(self.center, deg)
        self.F.rotateYaxis(self.center, deg)
        self.G.rotateYaxis(self.center, deg)
        self.H.rotateYaxis(self.center, deg)

    def rotateX(self, deg):

        self.A.rotateXaxis(self.center, deg)
        self.B.rotateXaxis(self.center, deg)
        self.C.rotateXaxis(self.center, deg)
        self.D.rotateXaxis(self.center, deg)
        self.E.rotateXaxis(self.center, deg)
        self.F.rotateXaxis(self.center, deg)
        self.G.rotateXaxis(self.center, deg)
        self.H.rotateXaxis(self.center, deg)

    def moveX(self, dist):


        self.A.add(Point(dist, 0, 0))
        self.B.add(Point(dist, 0, 0))
        self.C.add(Point(dist, 0, 0))
        self.D.add(Point(dist, 0, 0))
        self.E.add(Point(dist, 0, 0))
        self.F.add(Point(dist, 0, 0))
        self.G.add(Point(dist, 0, 0))
        self.H.add(Point(dist, 0, 0))
        self.center.add(Point(dist, 0, 0))

    def moveY(self, dist):


        self.A.add(Point(0, dist, 0))
        self.B.add(Point(0, dist, 0))
        self.C.add(Point(0, dist, 0))
        self.D.add(Point(0, dist, 0))
        self.E.add(Point(0, dist, 0))
        self.F.add(Point(0, dist, 0))
        self.G.add(Point(0, dist, 0))
        self.H.add(Point(0, dist, 0))
        self.center.add(Point(0, dist, 0))

class Field:

    def __init__(self, point, player, x, y, z):

        self.player = player
        self.color = WHITE
        self.position = point
        self.gridPos = (x, y, z)
        self.radius = 100 / (self.position.z/2)
        self.hoverCursor = False
        self.x = int(self.position.project()[0])
        self.y = int(self.position.project()[1])

    def draw(self, win):

        if self.player == 0 and self.hoverCursor:
            self.color = GRAY
        else:
            self.setColor()

        pygame.draw.circle(win, self.color, (self.x, self.y), int(self.radius), 0)


    def update(self, win):

        self.x = int(self.position.project()[0])
        self.y = int(self.position.project()[1])
        self.radius = 100 / (self.position.z / 2)
        self.draw(win)

    def setPlayer(self, player):
        self.player = player


    def setHover(self, isHover):
        if isHover:
            self.hoverCursor = True
        else:
            self.hoverCursor = False

    def setColor(self):

        if self.player == 1:
            self.color = BLUE
        if self.player == 2:
            self.color = RED
        if self.player == 0:
            self.color = WHITE

    def getDepth(self):
        return self.position.getZ()

class Grid:

    def __init__(self):

        self.zoom = 30
        self.center = Point(0, 0, self.zoom)
        self.points = []
        for x in range(3):
            self.points.append([])
            for y in range(3):
                self.points[x].append([])
                for z in range(3):
                    self.points[x][y].append(0)

        self.dist = 10

        for x in range(3):
            for y in range(3):
                for z in range(3):
                    self.points[x][y][z] = Point((- self.dist + x* self.dist),(- self.dist + y* self.dist),(self.zoom- self.dist + z* self.dist))

    def draw(self, win):

        pygame.draw.aaline(win, BLACK, self.points[0][0][0].project(), self.points[2][0][0].project(), 1)
        pygame.draw.aaline(win, BLACK, self.points[0][0][0].project(), self.points[0][2][0].project(), 1)
        pygame.draw.aaline(win, BLACK, self.points[2][2][0].project(), self.points[0][2][0].project(), 1)
        pygame.draw.aaline(win, BLACK, self.points[2][2][0].project(), self.points[2][0][0].project(), 1)
        pygame.draw.aaline(win, BLACK, self.points[1][1][0].project(), self.points[0][1][0].project(), 1)
        pygame.draw.aaline(win, BLACK, self.points[1][1][0].project(), self.points[2][1][0].project(), 1)
        pygame.draw.aaline(win, BLACK, self.points[1][1][0].project(), self.points[1][2][0].project(), 1)
        pygame.draw.aaline(win, BLACK, self.points[1][1][0].project(), self.points[1][0][0].project(), 1)
        pygame.draw.aaline(win, BLACK, self.points[0][0][0].project(), self.points[2][2][0].project(), 1)
        pygame.draw.aaline(win, BLACK, self.points[2][0][0].project(), self.points[0][2][0].project(), 1)

        pygame.draw.aaline(win, BLACK, self.points[0][0][1].project(), self.points[2][0][1].project(), 1)
        pygame.draw.aaline(win, BLACK, self.points[0][0][1].project(), self.points[0][2][1].project(), 1)
        pygame.draw.aaline(win, BLACK, self.points[2][2][1].project(), self.points[0][2][1].project(), 1)
        pygame.draw.aaline(win, BLACK, self.points[2][2][1].project(), self.points[2][0][1].project(), 1)
        pygame.draw.aaline(win, BLACK, self.points[1][1][1].project(), self.points[0][1][1].project(), 1)
        pygame.draw.aaline(win, BLACK, self.points[1][1][1].project(), self.points[2][1][1].project(), 1)
        pygame.draw.aaline(win, BLACK, self.points[1][1][1].project(), self.points[1][2][1].project(), 1)
        pygame.draw.aaline(win, BLACK, self.points[1][1][1].project(), self.points[1][0][1].project(), 1)
        pygame.draw.aaline(win, BLACK, self.points[0][0][1].project(), self.points[2][2][1].project(), 1)
        pygame.draw.aaline(win, BLACK, self.points[2][0][1].project(), self.points[0][2][1].project(), 1)

        pygame.draw.aaline(win, BLACK, self.points[0][0][2].project(), self.points[2][0][2].project(), 1)
        pygame.draw.aaline(win, BLACK, self.points[0][0][2].project(), self.points[0][2][2].project(), 1)
        pygame.draw.aaline(win, BLACK, self.points[2][2][2].project(), self.points[0][2][2].project(), 1)
        pygame.draw.aaline(win, BLACK, self.points[2][2][2].project(), self.points[2][0][2].project(), 1)
        pygame.draw.aaline(win, BLACK, self.points[1][1][2].project(), self.points[0][1][2].project(), 1)
        pygame.draw.aaline(win, BLACK, self.points[1][1][2].project(), self.points[2][1][2].project(), 1)
        pygame.draw.aaline(win, BLACK, self.points[1][1][2].project(), self.points[1][2][2].project(), 1)
        pygame.draw.aaline(win, BLACK, self.points[1][1][2].project(), self.points[1][0][2].project(), 1)
        pygame.draw.aaline(win, BLACK, self.points[0][0][2].project(), self.points[2][2][2].project(), 1)
        pygame.draw.aaline(win, BLACK, self.points[2][0][2].project(), self.points[0][2][2].project(), 1)

        pygame.draw.aaline(win, BLACK, self.points[0][0][0].project(), self.points[0][0][2].project(), 1)
        pygame.draw.aaline(win, BLACK, self.points[0][1][0].project(), self.points[0][1][2].project(), 1)
        pygame.draw.aaline(win, BLACK, self.points[0][2][0].project(), self.points[0][2][2].project(), 1)
        pygame.draw.aaline(win, BLACK, self.points[0][0][0].project(), self.points[0][2][2].project(), 1)
        pygame.draw.aaline(win, BLACK, self.points[0][2][0].project(), self.points[0][0][2].project(), 1)

        pygame.draw.aaline(win, BLACK, self.points[1][0][0].project(), self.points[1][0][2].project(), 1)
        pygame.draw.aaline(win, BLACK, self.points[1][1][0].project(), self.points[1][1][2].project(), 1)
        pygame.draw.aaline(win, BLACK, self.points[1][2][0].project(), self.points[1][2][2].project(), 1)
        pygame.draw.aaline(win, BLACK, self.points[1][0][0].project(), self.points[1][2][2].project(), 1)
        pygame.draw.aaline(win, BLACK, self.points[1][2][0].project(), self.points[1][0][2].project(), 1)

        pygame.draw.aaline(win, BLACK, self.points[2][0][0].project(), self.points[2][0][2].project(), 1)
        pygame.draw.aaline(win, BLACK, self.points[2][1][0].project(), self.points[2][1][2].project(), 1)
        pygame.draw.aaline(win, BLACK, self.points[2][2][0].project(), self.points[2][2][2].project(), 1)
        pygame.draw.aaline(win, BLACK, self.points[2][0][0].project(), self.points[2][2][2].project(), 1)
        pygame.draw.aaline(win, BLACK, self.points[2][2][0].project(), self.points[2][0][2].project(), 1)

        pygame.draw.aaline(win, BLACK, self.points[0][0][0].project(), self.points[2][0][2].project(), 1)
        pygame.draw.aaline(win, BLACK, self.points[2][0][0].project(), self.points[0][0][2].project(), 1)

        pygame.draw.aaline(win, BLACK, self.points[0][1][0].project(), self.points[2][1][2].project(), 1)
        pygame.draw.aaline(win, BLACK, self.points[2][1][0].project(), self.points[0][1][2].project(), 1)

        pygame.draw.aaline(win, BLACK, self.points[0][2][0].project(), self.points[2][2][2].project(), 1)
        pygame.draw.aaline(win, BLACK, self.points[2][2][0].project(), self.points[0][2][2].project(), 1)

        pygame.draw.aaline(win, BLACK, self.points[0][0][0].project(), self.points[2][2][2].project(), 1)
        pygame.draw.aaline(win, BLACK, self.points[0][2][0].project(), self.points[2][0][2].project(), 1)
        pygame.draw.aaline(win, BLACK, self.points[2][2][0].project(), self.points[0][0][2].project(), 1)
        pygame.draw.aaline(win, BLACK, self.points[2][0][0].project(), self.points[0][2][2].project(), 1)

    def rotateY(self, deg):
        for x in range(3):
            for y in range(3):
                for z in range(3):
                    self.points[x][y][z].rotateYaxis(self.center, deg)

    def rotateX(self, deg):
        for x in range(3):
            for y in range(3):
                for z in range(3):
                    self.points[x][y][z].rotateXaxis(self.center, deg)

    def rotateZ(self, deg):
        for x in range(3):
            for y in range(3):
                for z in range(3):
                    self.points[x][y][z].rotateZaxis(self.center, deg)

    def zoomIn(self):
        if self.zoom >= 20:
            self.zoom -= 1
            for x in range(3):
                for y in range(3):
                    for z in range(3):
                        self.points[x][y][z].add(Point(0, 0, -1))
            self.center.add(Point(0, 0, -1))


    def zoomOut(self):
        if self.zoom <= 100:
            self.zoom += 1
            for x in range(3):
                for y in range(3):
                    for z in range(3):
                        self.points[x][y][z].add(Point(0, 0, 1))
            self.center.add(Point(0, 0, 1))

class Label:

    def __init__(self, text, size = 18):

        pygame.font.init()
        self.font = pygame.font.SysFont('Calibri', size)
        self.font.set_bold(True)
        self.text = text
        self.surface = self.font.render(self.text, False, (0, 0, 0))

class Sphere:

    def __init__(self):

        self.img = pygame.image.load('img/yellow.png')

    def draw(self, win, scale, color):
        if color == "red":
            self.img = pygame.image.load('img/red.png')
        if color == "blue":
            self.img = pygame.image.load('img/red.png')

        self.img = pygame.transform.scale(self.img, (200/scale, 200/scale))
        win.blit(self.img, (300, 300))
