from View import*
from Model import*

def getDistance(x0, y0, x1, y1):
    x = x0 - x1
    y = y0 - y1

    return math.sqrt(x ** 2 + y ** 2)

def sort(array):#insertion sort

    i = 1
    j = 0

    for item in array[1:]:
        key = item
        while j >= 0 and array[j].getDepth() < key.getDepth():
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key
        i +=1
        j = i-1

class GameTable:

    def __init__(self):

        self.grid = Grid()
        self.engine = Engine()
        self.fields = []
        for x in range(3):
            for y in range(3):
                for z in range(3):
                    self.fields.append(Field(self.grid.points[x][y][z], 0, x, y, z))
        sort(self.fields)

    def draw(self, win):
        userInput = pygame.key.get_pressed()
        leftClick = pygame.mouse.get_pressed()[0]

        if (self.engine.winner != 0):

            self.grid.draw(win)
            for field in self.fields:
                field.setPlayer(self.engine.dataMatrix[field.gridPos[0]][field.gridPos[1]][field.gridPos[2]])
                field.update(win)
            playerText = ""
            if self.engine.winner == 1:
                playerText = "Player One (blue) won!"
            elif self.engine.winner == 2:
                playerText = "Player Two (red) won!"
            else:
                playerText = "Draw!"
            infoLabel = Label(playerText, 24)
            win.blit(infoLabel.surface, (250, 5))
        else:

            playerText = ""
            if self.engine.actualPlayer == 1:
                playerText = "Next player: Player One (blue)"
            else:
                playerText = "Next player: Player Two (red)"

            infoLabel = Label(playerText)
            win.blit(infoLabel.surface, (5,5))
            mousePos = (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

            activeField = False
            self.grid.draw(win)

            for field in self.fields:
                if field.radius > getDistance(mousePos[0], mousePos[1], field.x, field.y) and not activeField:
                    field.setHover(True)
                    if leftClick:
                        self.engine.step(field.gridPos[0], field.gridPos[1], field.gridPos[2])
                    activeField = True
                else:
                    field.setHover(False)
                field.setPlayer(self.engine.dataMatrix[field.gridPos[0]][field.gridPos[1]][field.gridPos[2]])
                field.update(win)

        if userInput[pygame.K_a]:
            self.grid.rotateY(-0.5)
            sort(self.fields)
        if userInput[pygame.K_d]:
            self.grid.rotateY(0.5)
            sort(self.fields)
        if userInput[pygame.K_w]:
            self.grid.rotateX(-0.5)
            sort(self.fields)
        if userInput[pygame.K_s]:
            self.grid.rotateX(0.5)
            sort(self.fields)
        if userInput[pygame.K_q]:
            self.grid.rotateZ(-0.5)
            sort(self.fields)
        if userInput[pygame.K_e]:
            self.grid.rotateZ(0.5)
            sort(self.fields)
        if userInput[pygame.K_UP]:
            self.grid.zoomIn()
        if userInput[pygame.K_DOWN]:
            self.grid.zoomOut()

def run():
    gameTable = GameTable()

    running = True
    while running:
        pygame.event.get()
        pygame.time.delay(5)
        window.fill((150, 210, 150))

        gameTable.draw(window)

        keyPressed = pygame.key.get_pressed()
        if keyPressed[pygame.K_ESCAPE]:
            running = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()

    pygame.quit()
