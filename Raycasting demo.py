from cmu_112_graphics import*
import math
#Source: https://pythonprogramming.altervista.org/raycasting-with-pygame/
#https://www.youtube.com/watch?v=gYRrGTC7GtA&t=498s

maze = [['w', 'c', 'w', 'w', 'w'],
        ['w', 'c', 'c', 'c', 'w'], 
        ['w', 'c', 'w', 'c', 'w'], 
        ['w', 'c', 'c', 'c', 'w'], 
        ['w', 'w', 'w', 'c', 'w']]

def appStarted(app):
    app.dimensions = 5
    app.drawMaze = True
    app.maze = maze
    app.px = app.height/4
    app.py = app.width/4
    app.pdx = 0
    app.pdy = 0
    app.pa = 0.1
    app.r = 5
    app.cellSize = 100
    app.squareX = app.height//app.dimensions
    app.squareY = app.width // app.dimensions

def keyPressed(app, event):
    #move
    if (event.key == 'a'):
        app.px -= 5
        if not isLegal(app):
            app.px += 5
    if (event.key == 'd'):
        app.px += 5
        if not isLegal(app):
            app.px -= 5
    if (event.key == 'w'):
        app.py -= 5
        if not isLegal(app):
            app.py += 5
    if (event.key == 's'):
        app.py += 5
        if not isLegal(app):
            app.py -= 5

    #look around
    if (event.key == 'Left'):
        app.pa -= 0.3
        if app.pa <= 0:
            app.pa += 2 * math.pi
        app.pdx = math.cos(app.pa) * 5
        app.pdy = math.sin(app.pa) * 5

    if (event.key == 'Right'):
        app.pa += 0.3
        if app.pa > 2 * math.pi:
            app.pa -= 2 * math.pi
        app.pdx = math.cos(app.pa) * 5
        app.pdy = math.sin(app.pa) * 5

    if (event.key == 'Up'):
        app.px += app.pdx
        app.py += app.pdy
        if not isLegal(app):
            app.px -= app.pdx
            app.py -= app.pdy

    if (event.key == 'Down'):
        app.px -= app.pdx
        app.py -= app.pdy
        if not isLegal(app):
            app.px += app.pdx
            app.py += app.pdy

def isLegal(app):
    playerRow = int(app.py // app.squareX)
    playerCol = int(app.px // app.squareY)
    if app.maze[playerRow][playerCol] == 'w':
        return False
    return True

def drawMaze(app, canvas):
    for i in range(len(app.maze)):
            for j in range(len(app.maze[0])):
                x0 = j * app.cellSize
                x1 = x0 + app.cellSize
                y0 = i * app.cellSize
                y1 = y0 + app.cellSize

                if app.maze[i][j] == 'w':
                    canvas.create_rectangle(x0,y0,x1,y1,fill = 'black')
                else:
                    canvas.create_rectangle(x0,y0,x1,y1,fill = 'white')

def drawRays(app, canvas):

    numberOfRays = 0
    mazeX = 0
    mazeY = 0
    mp = None
    rx, ry, ra, xo, yo = 0,0,0.1,0,0

    ra = app.pa
    aTan = -1/math.tan(ra)
    
    if ra > math.pi:
        ry = int(app.py/25)*25-0.0001
        rx = app.py-ry * aTan +app.px
        yo = -25
        xo = -yo * aTan
    if ra < math.pi:
        ry = int(app.py/25)*25+25
        rx = app.py-ry * aTan +app.px
        yo = 25
        xo = -yo * aTan
    if ra == 0 or ra == math.pi:
        rx = app.px
        ry = app.py
        numberOfRays = 8
    
    while numberOfRays < 8:
        mx = int(rx) / 25
        my = int(ry) /25
        mp = int(my * 5 + mx)
        if mp<5 and app.maze[mp] == 1:
            numberOfRays = 8
        else:
            rx += xo
            ry += yo
            numberOfRays += 1
        canvas.create_line(app.px, app.py, rx, ry,
        fill = 'blue', width = 1)

def redrawAll(app, canvas):
    drawRays(app,canvas)
    drawMaze(app, canvas)
    canvas.create_oval(app.px-app.r, app.py-app.r,
                       app.px+app.r, app.py+app.r,
                       fill='darkGreen')
    canvas.create_line(app.px, app.py, app.px+app.pdx * 10, app.py+app.pdy * 10,
     fill = 'black', width = 3)
    drawRays(app, canvas)

runApp(width=500, height=500)


# def drawRays(app, canvas):
#     mazeX = 0
#     mazeY = 0
#     mp = 0
#     ra = app.pa
#     rx = 0
#     ry = 0
#     dof = 0
#     xOffset = 0
#     yOffset = 0
#     aTan = -1/math.tan(ra)
#     if ra > math.pi:
#         ry = (int(app.py) / app.squareY) * app.squareY - .0001
#         rx = app.py-ry * aTan +app.px
#         yOffset = -app.squareX
#         xOffset = -yOffset * aTan
    
#     if ra < math.pi:
#         ry = (int(app.py) / app.squareY) * app.squareY + app.squareX
#         rx = app.py-ry * aTan +app.px
#         yOffset = app.squareX
#         xOffset = -yOffset * aTan
    
#     if ra == 0 or ra == math.pi:
#         rx = app.px
#         ry = app.py
#         dof = 8

#     while dof<8:
#         mazeX = int(rx/app.squareX)
#         mazeY = int(rx/app.squareY)
#         mp = mazeY * app.dimensions + mazeX
#         print(mazeX, mazeY)
#         if (mp< mazeX * mazeY and maze[mazeX][mazeY]=='w'):
#             dof = 8
#         else:
#             rx += xOffset
#             ry += yOffset
#             dof += 1


