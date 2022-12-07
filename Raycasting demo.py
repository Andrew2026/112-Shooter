from cmu_112_graphics import*
import math, random

#Source:
#https://weblog.jamisbuck.org/2011/1/27/maze-generation-growing-tree-algorithm
#https://medium.com/swlh/fun-with-python-1-maze-generator-931639b4fb7e 
#https://pythonprogramming.altervista.org/raycasting-with-pygame/
#https://youtu.be/eBFOjriHMc8 
#https://www.youtube.com/watch?v=gYRrGTC7GtA&t=498s

class Maze():
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.maze = []
        self.walls = []
        self.start = None
        self.end = None
        self.startHeight = 0
        self.startWidth = 0
        self.keyHeight = 0
        self.keyWidth = 0
        #initialize maze
        for row in range(0, height):
            line = []
            for col in range(0, width):
                line.append('u')
            self.maze.append(line)

    def createMaze(self):
        self.startHeight = random.randint(0, 1)
        if self.startHeight == 0:
            self.startHeight = 1
        else:
            self.startHeight = self.height - 2
        
        self.startWidth = random.randint(0, 1)
        if self.startWidth == 0:
            self.startWidth = 1
        else:
            self.startWidth = self.width - 2

        if self.startHeight == 1 and self.startWidth == 1:
            self.startWidth = self.width - 2

        self.maze[self.startHeight][self.startWidth] = 0
        self.maze[self.startHeight-1][self.startWidth] = 1
        self.maze[self.startHeight][self.startWidth-1] = 1
        self.maze[self.startHeight][self.startWidth+1] = 1
        self.maze[self.startHeight+1][self.startWidth] = 1

        self.walls.append([self.startHeight-1, self.startWidth] )
        self.walls.append([self.startHeight, self.startWidth-1])
        self.walls.append([self.startHeight, self.startWidth+1])
        self.walls.append([self.startHeight+1, self.startWidth])

        #while there are still walls
        while self.walls != []:
            #select random wall
            randomWall = self.walls[random.randint(0,len(self.walls)-1)]
            #check if wall is a border wall
            if randomWall[0] != 0:
                #check if wall has neighbors
                if (self.maze[randomWall[0]-1][randomWall[1]] == 'u' and 
                self.maze[randomWall[0]+1][randomWall[1]] == 0):
                    if self.surroundingCells(randomWall) < 2:
                        self.maze[randomWall[0]][randomWall[1]] = 0
                        #make neightbors walls
                        if (randomWall[1] != 0):
                            if self.maze[randomWall[0]][randomWall[1]-1] != 0:
                                self.maze[randomWall[0]][randomWall[1]-1] = 1
                            if [randomWall[0], randomWall[1]-1] not in self.walls:
                                self.walls.append([randomWall[0], randomWall[1]-1])

                        if(randomWall[1] != self.width -1):
                            if self.maze[randomWall[0]][randomWall[1]+1] != 0:
                                self.maze[randomWall[0]][randomWall[1]+1] = 1
                            if [randomWall[0], randomWall[1]+1] not in self.walls:
                                self.walls.append([randomWall[0], randomWall[1]+1])
                        
                        if self.maze[randomWall[0]-1][randomWall[1]] != 0:
                            self.maze[randomWall[0]-1][randomWall[1]] = 1
                        if [randomWall[0]-1, randomWall[1]] not in self.walls:
                            self.walls.append([randomWall[0]-1, randomWall[1]])

                  
            if randomWall[1] != 0:
                if (self.maze[randomWall[0]][randomWall[1]-1] == 'u' and 
                self.maze[randomWall[0]][randomWall[1]+1] == 0):
                    if self.surroundingCells(randomWall) < 2:
                        self.maze[randomWall[0]][randomWall[1]] = 0
                        if (randomWall[0] != 0):
                            if self.maze[randomWall[0]-1][randomWall[1]] != 0:
                                self.maze[randomWall[0]-1][randomWall[1]] = 1
                            if [randomWall[0]-1, randomWall[1]] not in self.walls:
                                self.walls.append([randomWall[0]-1,randomWall[1]])

                        if (randomWall[0] != self.height-1):
                            if self.maze[randomWall[0]+1][randomWall[1]] != 0:
                                self.maze[randomWall[0]+1][randomWall[1]] = 1
                            if [randomWall[0]+1, randomWall[1]] not in self.walls:
                                self.walls.append([randomWall[0]+1,randomWall[1]])

                            if self.maze[randomWall[0]][randomWall[1]-1] != 0:
                                self.maze[randomWall[0]][randomWall[1]-1] = 1
                            if [randomWall[0], randomWall[1]-1] not in self.walls:
                                self.walls.append([randomWall[0],randomWall[1]-1])
            
            if randomWall[0] != self.height-1:
                if (self.maze[randomWall[0]+1][randomWall[1]] == 'u' and 
                self.maze[randomWall[0]-1][randomWall[1]] == 0):
                    if self.surroundingCells(randomWall) < 2:
                        self.maze[randomWall[0]][randomWall[1]] = 0
                        if (randomWall[1] != self.width-1):
                            if self.maze[randomWall[0]][randomWall[1]+1] != 0:
                                self.maze[randomWall[0]][randomWall[1]+1] = 1
                            if [randomWall[0], randomWall[1]+1] not in self.walls:
                                self.walls.append([randomWall[0], randomWall[1]+1])

                        if (randomWall[1] != 0):
                            if self.maze[randomWall[0]][randomWall[1]-1] != 0:
                                self.maze[randomWall[0]][randomWall[1]-1] = 1
                            if [randomWall[0], randomWall[1]-1] not in self.walls:
                                self.walls.append([randomWall[0], randomWall[1]-1])
                        
                        if self.maze[randomWall[0]+1][randomWall[1]] != 0:
                            self.maze[randomWall[0]+1][randomWall[1]] = 1
                        if [randomWall[0]+1, randomWall[1]] not in self.walls:
                            self.walls.append([randomWall[0]+1, randomWall[1]])

                        
            if randomWall[1] != self.width - 1:
                if (self.maze[randomWall[0]][randomWall[1]+1] == 'u' and 
                self.maze[randomWall[0]][randomWall[1]-1] == 0):
                    if self.surroundingCells(randomWall) < 2:
                        self.maze[randomWall[0]][randomWall[1]] = 0

                        if (randomWall[0] != self.height-1):
                            if self.maze[randomWall[0]+1][randomWall[1]] != 0:
                                self.maze[randomWall[0]+1][randomWall[1]] = 1
                            if [randomWall[0]+1, randomWall[1]] not in self.walls:
                                self.walls.append([randomWall[0]+1,randomWall[1]])
                        
                        if (randomWall[0] != 0):
                            if self.maze[randomWall[0]-1][randomWall[1]] != 0:
                                self.maze[randomWall[0]-1][randomWall[1]] = 1
                            if [randomWall[0]-1, randomWall[1]] not in self.walls:
                                self.walls.append([randomWall[0]-1,randomWall[1]])
                        
                        if self.maze[randomWall[0]][randomWall[1]+1] != 0:
                            self.maze[randomWall[0]][randomWall[1]+1] = 1
                        if [randomWall[0], randomWall[1]+1] not in self.walls:
                            self.walls.append([randomWall[0],randomWall[1]+1])
 
            #delete wall that was made into cell
            self.deleteWall(randomWall) 

        #make border walls
        for row in range(0, self.height):
            for col in range(0, self.width):
                if (self.maze[row][col] == 'u'):
                    self.maze[row][col] = 1

        #create start and end
        for col in range(0, self.width):
            if (self.maze[1][col] == 0):
                self.maze[0][col] = 0
                self.start = [[0],[col]]
                break
        
        #create door
        for row in range(0, self.height):
            for col in range(0, self.width):
                if row == self.startHeight and col == self.startWidth:
                    if self.startHeight == 1 and self.startWidth == self.width - 2:
                            self.maze[2][self.width - 2] = 2
                            self.maze[1][self.width - 3] = 2

                    if self.startHeight == self.height - 2 and self.startWidth == 1:
                            self.maze[self.height - 3][1] = 2
                            self.maze[self.height - 2][2] = 2

                    if self.startHeight == self.height - 2 and self.startWidth == self.width - 2:
                            self.maze[self.height - 3][self.width - 2] = 2
                            self.maze[self.height - 2][self.width - 3] = 2

        #create key
        self.keyHeight = random.randint(self.height/2, self.height - 2)
        for i in range(self.width - 2):
            if self.maze[self.keyHeight][i] == 0:
                self.maze[self.keyHeight][i] = 3
                self.keyWidth = i
                break

    def print(self):
        print (self.maze)

    def surroundingCells(self, randomWall):
        numberOfCells = 0
        if (self.maze[randomWall[0]-1][randomWall[1]] == 0 or
            self.maze[randomWall[0]+1][randomWall[1]] == 0 or
            self.maze[randomWall[0]][randomWall[1]-1] == 0 or
            self.maze[randomWall[0]][randomWall[1]+1] == 0):
            numberOfCells += 1

        return numberOfCells

    def deleteWall(self, randomWall):
        for wall in self.walls:
            if (wall[0], wall[1]) == (randomWall[0], randomWall[1]):
                self.walls.remove(wall)

def appStarted(app):
    a = Maze(20,20)
    a.createMaze()
    app.maze = a.maze
    app.startHeight = a.startHeight
    app.startWidth = a.startWidth
    app.keyHeight = a.keyHeight
    app.keyWidth = a.keyWidth
    app.dimensions = len(app.maze)
    app.cellSize = app.height/app.dimensions
    app.mazeXO = app.width/2 // app.dimensions
    app.mazeYO = app.height // app.dimensions
    for row in range(len(app.maze)):
        for col in range(len(app.maze[0])):
            if app.maze[row][col] == 0:
                app.px = col * app.mazeXO + app.cellSize/2
                app.py = row * app.mazeYO + app.cellSize/2
                break
        break
    app.pdx = 0
    app.pdy = 0
    app.pa = 1.0005
    app.playerR = 5
    app.gameOver = False
    app.preMouseX = 0
    app.doorUnlocked = False

def keyPressed(app, event):

    #move
    if (event.key == 'a'):
        if 0 < app.pa < math.pi/2:
            app.px += app.pdy / (app.dimensions / 5)
            app.py -= app.pdx  / (app.dimensions / 5)
            if not isLegal(app):
                app.px -= app.pdy / (app.dimensions / 5)
                app.py += app.pdx / (app.dimensions / 5)
        if math.pi/2 < app.pa < math.pi:
            app.px += app.pdy / (app.dimensions / 5)
            app.py -= app.pdx / (app.dimensions / 5)
            if not isLegal(app):
                app.px -= app.pdy / (app.dimensions / 5)
                app.py += app.pdx / (app.dimensions / 5)
        if math.pi < app.pa < 3 * math.pi / 2:
            app.px += app.pdy / (app.dimensions / 5)
            app.py -= app.pdx / (app.dimensions / 5)
            if not isLegal(app):
                app.px -= app.pdy / (app.dimensions / 5)
                app.py += app.pdx / (app.dimensions / 5)
        if 3 * math.pi/2 < app.pa < 2 * math.pi:
            app.px += app.pdy / (app.dimensions / 5)
            app.py -= app.pdx / (app.dimensions / 5)
            if not isLegal(app):
                app.px -= app.pdy / (app.dimensions / 5)
                app.py += app.pdx / (app.dimensions / 5)
        if app.pa == math.pi/2:
            app.px -= app.py / (app.dimensions / 5)
            app.py -= app.px / (app.dimensions / 5)
            if not isLegal(app):
                app.px += app.pdy / (app.dimensions / 5)
                app.py += app.pdx / (app.dimensions / 5)
        if app.pa == 3 * math.pi/2:
            app.px += app.py / (app.dimensions / 5)
            app.py += app.px / (app.dimensions / 5)
            if not isLegal(app):
                app.px -= app.pdy / (app.dimensions / 5)
                app.py -= app.pdx / (app.dimensions / 5)

        playerRow = int(app.py // app.mazeYO)
        playerCol = int(app.px // app.mazeXO)
        if (playerRow, playerCol) == (app.startHeight, app.startWidth):
            app.gameOver = True
        
        
        if playerRow == (app.keyWidth - 1):
            if playerCol == app.keyHeight - 1:
                app.maze[app.keyHeight][app.keyWidth] = 1
                app.doorUnlocked = True
            if playerCol == app.keyHeight + 1:
                app.maze[app.keyHeight][app.keyWidth] = 1
                app.doorUnlocked = True

        if playerRow == app.keyWidth + 1:
            if playerCol == app.keyHeight - 1:
                app.maze[app.keyHeight][app.keyWidth] = 1
                app.doorUnlocked = True
            if playerCol == app.keyHeight + 1:
                app.maze[app.keyHeight][app.keyWidth] = 1
                app.doorUnlocked = True

    if (event.key == 'd'):
        if 0 < app.pa < math.pi/2:
            app.px -= app.pdy / (app.dimensions / 5)
            app.py += app.pdx  / (app.dimensions / 5)
            if not isLegal(app):
                app.px += app.pdy / (app.dimensions / 5)
                app.py -= app.pdx / (app.dimensions / 5)
        if math.pi/2 < app.pa < math.pi:
            app.px -= app.pdy / (app.dimensions / 5)
            app.py += app.pdx / (app.dimensions / 5)
            if not isLegal(app):
                app.px += app.pdy / (app.dimensions / 5)
                app.py -= app.pdx / (app.dimensions / 5)
        if math.pi < app.pa < 3 * math.pi / 2:
            app.px -= app.pdy / (app.dimensions / 5)
            app.py += app.pdx / (app.dimensions / 5)
            if not isLegal(app):
                app.px += app.pdy / (app.dimensions / 5)
                app.py -= app.pdx / (app.dimensions / 5)
        if 3 * math.pi/2 < app.pa < 2 * math.pi:
            app.px -= app.pdy / (app.dimensions / 5)
            app.py += app.pdx / (app.dimensions / 5)
            if not isLegal(app):
                app.px += app.pdy / (app.dimensions / 5)
                app.py -= app.pdx / (app.dimensions / 5)
        if app.pa == math.pi/2:
            app.px += app.py / (app.dimensions / 5)
            app.py += app.px / (app.dimensions / 5)
            if not isLegal(app):
                app.px -= app.pdy / (app.dimensions / 5)
                app.py -= app.pdx / (app.dimensions / 5)
        if app.pa == 3 * math.pi/2:
            app.px -= app.py / (app.dimensions / 5)
            app.py -= app.px / (app.dimensions / 5)
            if not isLegal(app):
                app.px += app.pdy / (app.dimensions / 5)
                app.py += app.pdx / (app.dimensions / 5)
        
        playerRow = int(app.py // app.mazeYO)
        playerCol = int(app.px // app.mazeXO)
        if (playerRow, playerCol) == (len(app.maze) - 2, len(app.maze[0]) - 2):
            app.gameOver = True

        
        if playerRow == (app.keyWidth - 1):
            if playerCol == app.keyHeight - 1:
                app.maze[app.keyHeight][app.keyWidth] = 1
                app.doorUnlocked = True
            if playerCol == app.keyHeight + 1:
                app.maze[app.keyHeight][app.keyWidth] = 1
                app.doorUnlocked = True

        if playerRow == app.keyWidth + 1:
            if playerCol == app.keyHeight - 1:
                app.maze[app.keyHeight][app.keyWidth] = 1
                app.doorUnlocked = True
            if playerCol == app.keyHeight + 1:
                app.maze[app.keyHeight][app.keyWidth] = 1
                app.doorUnlocked = True
            

    if (event.key == 'w'):
        app.px += app.pdx #/ (app.dimensions / 5)
        app.py += app.pdy #/ (app.dimensions / 5)
        if not isLegal(app):
            app.px -= app.pdx #/ (app.dimensions / 5)
            app.py -= app.pdy #/ (app.dimensions / 5)
        playerRow = int(app.py // app.mazeYO)
        playerCol = int(app.px // app.mazeXO)
        if (playerRow, playerCol) == (len(app.maze) - 2, len(app.maze[0]) - 2):
            app.gameOver = True

        if playerRow == (app.keyWidth - 1):
            if playerCol == app.keyHeight - 1:
                app.maze[app.keyHeight][app.keyWidth] = 1
                app.doorUnlocked = True
            if playerCol == app.keyHeight + 1:
                app.maze[app.keyHeight][app.keyWidth] = 1
                app.doorUnlocked = True

        if playerRow == app.keyWidth + 1:
            if playerCol == app.keyHeight - 1:
                app.maze[app.keyHeight][app.keyWidth] = 1
                app.doorUnlocked = True
            if playerCol == app.keyHeight + 1:
                app.maze[app.keyHeight][app.keyWidth] = 1
                app.doorUnlocked = True

            

    if (event.key == 's'):
        app.px -= app.pdx / (app.dimensions / 5)
        app.py -= app.pdy / (app.dimensions / 5)
        if not isLegal(app):
            app.px += app.pdx / (app.dimensions / 5)
            app.py += app.pdy / (app.dimensions / 5)
        playerRow = int(app.py // app.mazeYO)
        playerCol = int(app.px // app.mazeXO)
        if (playerRow, playerCol) == (app.startHeight, app.startWidth):
            app.gameOver = True

        
        if playerRow == (app.keyWidth - 1):
            if playerCol == app.keyHeight - 1:
                app.maze[app.keyHeight][app.keyWidth] = 1
                app.doorUnlocked = True
            if playerCol == app.keyHeight + 1:
                app.maze[app.keyHeight][app.keyWidth] = 1
                app.doorUnlocked = True

        if playerRow == app.keyWidth + 1:
            if playerCol == app.keyHeight - 1:
                app.maze[app.keyHeight][app.keyWidth] = 1
                app.doorUnlocked = True
            if playerCol == app.keyHeight + 1:
                app.maze[app.keyHeight][app.keyWidth] = 1
                app.doorUnlocked = True

    if (event.key == 'e'):
        if app.startHeight == 1:
                app.maze[app.startHeight+1][app.startWidth] = 0
                app.maze[app.startHeight][app.startWidth-1] = 0
        
        if app.startWidth == 1:
                app.maze[app.startHeight][app.startWidth+1] = 0
                app.maze[app.startHeight-1][app.startWidth] = 0

        if app.startWidth == len(app.maze) - 2 and app.startHeight == len(app.
        maze[0]) - 2:
                app.maze[app.startHeight-1][app.startWidth] = 0
                app.maze[app.startHeight][app.startWidth-1] = 0

    if (event.key == 'r'):
        if app.gameOver == True:
            appStarted(app)

#look
def mouseMoved(app, event):
    if event.x < app.preMouseX:
        app.pa -= (0.01 + 0.05 * (app.preMouseX - event.x))
        if app.pa < 0:
            app.pa += 2 * math.pi
        app.pdx = math.cos(app.pa) * 5
        app.pdy = math.sin(app.pa) * 5
        playerRow = int(app.py // app.mazeYO)
        playerCol = int(app.px // app.mazeXO)
        if (playerRow, playerCol) == (len(app.maze) - 2, len(app.maze[0]) - 2):
            app.gameOver = True

    if event.x > app.preMouseX:
        app.pa += (0.01 + 0.02 * (event.x - app.preMouseX))
        if app.pa > 2 * math.pi:
            app.pa -= 2 * math.pi
        app.pdx = math.cos(app.pa) * 5
        app.pdy = math.sin(app.pa) * 5
        playerRow = int(app.py // app.mazeYO)
        playerCol = int(app.px // app.mazeXO)
        if (playerRow, playerCol) == (len(app.maze) - 2, len(app.maze[0]) - 2):
            app.gameOver = True

    app.preMouseX = event.x

def isLegal(app):
    playerRow = int(app.py // app.mazeYO)
    playerCol = int(app.px // app.mazeXO)
    if playerRow >= app.dimensions or playerCol >= app.dimensions:
        return False
    if app.maze[playerRow][playerCol] != 0:
        return False
    return True

def getDistance(px, py, rx, ry):
    return math.sqrt((rx - px)**2 + (ry - py)**2)

def drawBackground(app, canvas):
    canvas.create_rectangle(0, 0, app.width, app.height/2, fill = 'sky blue')
    canvas.create_rectangle(0, app.height/2, app.width, app.height, 
    fill = 'saddlebrown')

def drawMaze(app, canvas):
    for i in range(len(app.maze)):
            for j in range(len(app.maze[0])):
                x0 = j * app.cellSize
                x1 = x0 + app.cellSize
                y0 = i * app.cellSize
                y1 = y0 + app.cellSize
                if (i, j) == (app.startHeight, app.startWidth):
                    canvas.create_rectangle(x0, y0, x1, y1, fill = 'green')
                elif app.maze[i][j] == 3:
                    canvas.create_rectangle(x0 + app.cellSize/3, y0 + 
                    app.cellSize/3, x1 - app.cellSize/3, y1 - app.cellSize/3, 
                    fill = 'yellow')
                elif app.maze[i][j] != 0:
                    canvas.create_rectangle(x0, y0, x1, y1, fill = 'black')
                else:
                    canvas.create_rectangle(x0, y0, x1, y1, fill = 'white')

def drawPlayer(app, canvas):
    canvas.create_rectangle(app.px - app.playerR, app.py - app.playerR,
                       app.px + app.playerR, app.py + app.playerR,
                       fill = 'darkGreen')
    canvas.create_line(app.px, app.py, app.px + app.pdx * 5, app.py + 
    app.pdy * 5, fill = 'black', width = 2)
    
def checkHorizontal(app, ra):
    xo, yo, rx, ry, cellsChecked, distH = 0, 0, 0, 0, 0, 0
    aTan = -1/math.tan(ra)

    #looking up
    if ra > math.pi:
        ry = int(app.py // app.mazeYO) * app.mazeYO
        rx = (app.py - ry) * aTan + app.px
        yo = -app.mazeYO
        xo = -yo * aTan

    #looking down
    if ra < math.pi:
        ry = (int(app.py // app.mazeYO) + 1) * app.mazeYO
        rx = (app.py - ry) * aTan + app.px
        yo = app.mazeYO
        xo = -yo * aTan
    
    #can't hit horizontal wall
    if ra == 0 or ra == math.pi:
        rx = app.px
        ry = app.py
        cellsChecked = app.dimensions
    
    #while ray did not hit wall
    while cellsChecked < app.dimensions:
        rayRow = int(ry // app.mazeYO)
        rayCol = int(rx // app.mazeXO)

        #looking down
        if ra < math.pi:
            if (rayRow < app.dimensions and rayCol < app.dimensions and 
            rayRow >= 0 and rayCol >= 0 and app.maze[rayRow][rayCol] != 0):
                cellsChecked = app.dimensions
                distH = getDistance(app.px, app.py, rx, ry)
            else:
                rx += xo
                ry += yo
                cellsChecked += 1

        #looking up
        else:
            if (rayRow < app.dimensions and rayCol < app.dimensions and 
            rayRow >= 0 and rayCol >= 0 and app.maze[rayRow-1][rayCol] != 0):
                cellsChecked = app.dimensions
                distH = getDistance(app.px, app.py, rx, ry)
            else:
                rx += xo
                ry += yo
                cellsChecked += 1

    return (distH, rx, ry, ra)
    

def checkVertical(app, ra):
    xo, yo, rx, ry, cellsChecked, distV = 0, 0, 0, 0, 0, 0   
    nTan = -math.tan(ra)

    #looking left
    if ra > math.pi/2 and ra < 3*math.pi/2:
        rx = int(app.px // app.mazeXO) * app.mazeXO
        ry = (app.px - rx) * nTan + app.py
        xo = -app.mazeXO
        yo = -xo * nTan

    #looking right
    if ra < math.pi/2 or ra > 3*math.pi/2:
        rx = (int(app.px // app.mazeXO) + 1) * app.mazeXO
        ry = (app.px - rx) * nTan + app.py
        xo = app.mazeXO
        yo = -xo * nTan
    
    #can't hit verticle wall
    if ra == 0 or ra == math.pi:
        rx = app.px
        ry = app.py
        cellsChecked = app.dimensions
    
    #while ray did not hit wall
    while cellsChecked < app.dimensions:
        rayRow = int(ry // app.mazeYO)
        rayCol = int(rx // app.mazeXO)

        #looking left
        if ra > math.pi/2 and ra < 3*math.pi/2:
            if (rayRow < app.dimensions and rayCol < app.dimensions and 
            rayRow >= 0 and rayCol >= 0 and app.maze[rayRow][rayCol-1] != 0):
                cellsChecked = app.dimensions
                distV = getDistance(app.px, app.py, rx, ry)
            else:
                rx += xo
                ry += yo
                cellsChecked += 1
        
        #looking right
        else:
            if (rayRow < app.dimensions and rayCol < app.dimensions and 
            rayRow >= 0 and rayCol >= 0 and app.maze[rayRow][rayCol] != 0):
                cellsChecked = app.dimensions
                distV = getDistance(app.px, app.py, rx, ry)
            else:
                rx += xo
                ry += yo
                cellsChecked += 1
    return (distV, rx, ry, ra)

def drawRays(app, canvas):
    #sDist = shortest Ray
    sDist = 0

    #set ray at 30 degree angle left of player
    ra = app.pa - math.pi/6

    #check bounds
    if ra < 0:
            ra += 2*math.pi
    if ra > 2 * math.pi:
            ra -= 2*math.pi

    for ray in range(90):
        (distH, xH, yH, ra) = checkHorizontal(app, ra)
        (distV, xV, yV, ra) = checkVertical(app, ra)
        rayHRow = int(yH // app.mazeYO)
        rayHCol = int(xH // app.mazeXO)
        rayVRow = int(yV // app.mazeYO)
        rayVCol = int(xV // app.mazeXO)

        if distH == 0:
            canvas.create_line(app.px, app.py, xV, yV, fill = 'green', 
            width = 1)
            sDist = distV
            #diff color for diff wall
            if ra > math.pi/2 and ra < 3*math.pi/2:
                if (rayVRow < app.dimensions and rayVCol < app.dimensions and 
                    rayVRow >= 0 and rayVCol >= 0):
                    if app.maze[rayVRow][rayVCol-1] == 1:
                        color = 'green'
                    if app.maze[rayVRow][rayVCol-1] == 2:
                        color = 'red'
                    if app.maze[rayVRow][rayVCol-1] == 3:
                        color = 'yellow'
                    if app.maze[rayVRow][rayVCol-1] == 4:
                        color = 'pink'
                    if app.maze[rayVRow][rayVCol-1] == 5:
                        color = 'purple'
            else:
                if (rayVRow < app.dimensions and rayVCol < app.dimensions and 
                rayVRow >= 0 and rayVCol >= 0):
                    if app.maze[rayVRow][rayVCol] == 1:
                        color = 'green'
                    if app.maze[rayVRow][rayVCol] == 2:
                        color = 'red'
                    if app.maze[rayVRow][rayVCol] == 3:
                        color = 'yellow'
                    if app.maze[rayVRow][rayVCol] == 4:
                        color = 'pink'
                    if app.maze[rayVRow][rayVCol] == 5:
                        color = 'purple'


        elif distV == 0:
            canvas.create_line(app.px, app.py, xH, yH, fill = 'green', 
            width = 1)
            sDist = distH
            #diff color for diff wall
            if ra < math.pi:
                if (rayHRow < app.dimensions and rayHCol < app.dimensions and 
                rayHRow >= 0 and rayHCol >= 0):
                    if app.maze[rayHRow][rayHCol] == 1:
                        color = 'green3'
                    if app.maze[rayHRow][rayHCol] == 2:
                        color = 'red3'
                    if app.maze[rayHRow][rayHCol] == 3:
                        color = 'yellow3'
                    if app.maze[rayHRow][rayHCol] == 4:
                        color = 'pink3'
                    if app.maze[rayHRow][rayHCol] == 5:
                        color = 'purple3'
            else:
                if (rayHRow < app.dimensions and rayHCol < app.dimensions and 
                rayHRow >= 0 and rayHCol >= 0):
                    if app.maze[rayHRow-1][rayHCol] == 1:
                        color = 'green3'
                    if app.maze[rayHRow-1][rayHCol] == 2:
                        color = 'red3'
                    if app.maze[rayHRow-1][rayHCol] == 3:
                        color = 'yellow3'
                    if app.maze[rayHRow-1][rayHCol] == 4:
                        color = 'pink3'
                    if app.maze[rayHRow-1][rayHCol] == 5:
                        color = 'purple3'

        elif distH > distV:
            canvas.create_line(app.px, app.py, xV, yV, fill = 'green', 
            width = 1)
            sDist = distV
            #diff color for diff wall
            if ra > math.pi/2 and ra < 3*math.pi/2:
                if (rayVRow < app.dimensions and rayVCol < app.dimensions and 
                rayVRow >= 0 and rayVCol >= 0):
                    if app.maze[rayVRow][rayVCol-1] == 1:
                        color = 'green'
                    if app.maze[rayVRow][rayVCol-1] == 2:
                        color = 'red'
                    if app.maze[rayVRow][rayVCol-1] == 3:
                        color = 'yellow'
                    if app.maze[rayVRow][rayVCol-1] == 4:
                        color = 'pink'
                    if app.maze[rayVRow][rayVCol-1] == 5:
                        color = 'purple'
            else:
                if (rayVRow < app.dimensions and rayVCol < app.dimensions and 
                rayVRow >= 0 and rayVCol >= 0):
                    if app.maze[rayVRow][rayVCol] == 1:
                        color = 'green'
                    if app.maze[rayVRow][rayVCol] == 2:
                        color = 'red'
                    if app.maze[rayVRow][rayVCol] == 3:
                        color = 'yellow'
                    if app.maze[rayVRow][rayVCol] == 4:
                        color = 'pink'
                    if app.maze[rayVRow][rayVCol] == 5:
                        color = 'purple'

        else:
            canvas.create_line(app.px, app.py, xH, yH, fill = 'green', 
            width = 1)
            sDist = distH
            #diff color for diff wall
            if ra < math.pi:
                if (rayHRow < app.dimensions and rayHCol < app.dimensions and 
                rayHRow >= 0 and rayHCol >= 0):
                    if app.maze[rayHRow][rayHCol] == 1:
                        color = 'green3'
                    if app.maze[rayHRow][rayHCol] == 2:
                        color = 'red3'
                    if app.maze[rayHRow][rayHCol] == 3:
                        color = 'yellow3'
                    if app.maze[rayHRow][rayHCol] == 4:
                        color = 'pink3'
                    if app.maze[rayHRow][rayHCol] == 5:
                        color = 'purple3'
            else:
                if (rayHRow < app.dimensions and rayHCol < app.dimensions and 
                rayHRow >= 0 and rayHCol >= 0):
                    if app.maze[rayHRow-1][rayHCol] == 1:
                        color = 'green3'
                    if app.maze[rayHRow-1][rayHCol] == 2:
                        color = 'red3'
                    if app.maze[rayHRow-1][rayHCol] == 3:
                        color = 'yellow3'
                    if app.maze[rayHRow-1][rayHCol] == 4:
                        color = 'pink3'
                    if app.maze[rayHRow-1][rayHCol] == 5:
                        color = 'purple3'

        #check bounds again after addition
        ra += math.pi/270
        if ra < 0:
            ra += 2 * math.pi
        if ra > 2 * math.pi:
            ra -= 2 * math.pi

        #castAngle
        ca = app.pa - ra
        if ca < 0:
            ca += 2 * math.pi
        if ca > 2 * math.pi:
            ca -= 2 * math.pi

        #cos on castAngle to fix fisheye effect
        sDist = sDist * math.cos(ca)

        #height of each individual ray on wall
        height = (app.mazeXO * (340))/sDist

        #bound height
        if height > app.height:
            height == app.height

        #line offset to center casted walls on screen
        lineO = app.height/2 - height/2

        #draw walls
    
        canvas.create_line(ray * 8 + app.width/2, lineO, ray * 8 + app.height, 
        height + lineO, fill = color, width = 8)

def drawKey(app, canvas):
    a = key(300,300,20, True)
    if a.gameState == True:
        sx = a.x - app.px
        sy = a.y - app.py
        sz = a.z 

        CS =  math.cos(app.pa)
        SN =  math.sin(app.pa)

        x = sy * CS + sx * SN
        y = sx * CS - sy * SN

        # a = sx * CS - sy * SN
        # b = sx * SN + sy * CS

        sx = x + a.x
        sy = y + a.y
        
        sx = (sx*108.0/sy) + app.width/2
        sy = (sz*108.0/sx) + app.height/1.5
        if abs(app.px - a.x) < 30 or abs(app.py - a.y) < 30:
            a.gameState = False
            app.doorUnlocked = True
            
        canvas.create_rectangle(app.px + sx-4, app.py+sy-4, app.px+sx+4, app.py+sy+4,
        fill = 'yellow', width = 0)

def drawCrosshair(app, canvas):
    canvas.create_line(3 * app.width/4 - 15, app.height/2, 3 * app.width/4 + 15,
     app.height/2, fill = 'black', width = 1)
    canvas.create_line(3 * app.width/4, app.height/2 - 15, 3 * app.width/4,
     app.height/2 + 15, fill = 'black', width = 1)

def drawEndBanner(app, canvas):
    canvas.create_text(app.width/2, app.height/2, 
    text = 'You Win!!! (Press r to restart)', font = 'Arial 30', fill = 'Black')

def redrawAll(app, canvas):
    if app.gameOver:
        drawEndBanner(app, canvas)
    else:
        drawBackground(app,canvas)
        drawMaze(app, canvas)
        drawPlayer(app, canvas)
        drawRays(app, canvas)
        drawCrosshair(app, canvas)
        # drawKey(app, canvas)
        
        
class key():
    def __init__(self, x, y, z, gameState):
        self.x = x
        self.y = y
        self.z = z
        self.gameState = gameState

runApp(width = 1400, height = 700)




