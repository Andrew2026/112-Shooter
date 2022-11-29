from cmu_112_graphics import*
import math
import cs112_f22_week6_linter
import decimal

#Source: https://pythonprogramming.altervista.org/raycasting-with-pygame/
#https://www.youtube.com/watch?v=gYRrGTC7GtA&t=498s

#cmu112 Hw
def roundHalfUp(d):
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

maze = [['w', 'c', 'w', 'w', 'w', 'w', 'w', 'w'],
        ['w', 'c', 'c', 'w', 'w', 'c', 'c', 'w'], 
        ['w', 'w', 'c', 'w', 'w', 'c', 'w', 'w'], 
        ['w', 'c', 'c', 'c', 'c', 'c', 'c', 'w'], 
        ['w', 'c', 'c', 'c', 'w', 'c', 'c', 'w'], 
        ['w', 'c', 'w', 'w', 'w', 'w', 'c', 'w'], 
        ['w', 'c', 'c', 'c', 'w', 'c', 'c', 'w'], 
        ['w', 'w', 'w', 'w', 'w', 'w', 'c', 'w']]


def appStarted(app):
    app.dimensions = 8
    app.cellSize = 100
    app.maze = maze
    app.px = 150
    app.py = 150
    app.pdx = 0
    app.pdy = 0
    app.mazeXO = app.width // app.dimensions
    app.mazeYO = app.height // app.dimensions
    app.pa = 1.05
    app.playerR = 5

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
        app.pa -= 0.1
        if app.pa <= 0:
            app.pa += 2 * math.pi
        app.pdx = math.cos(app.pa) * 5
        app.pdy = math.sin(app.pa) * 5

    if (event.key == 'Right'):
        app.pa += 0.1
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
    playerRow = int(app.py // app.mazeYO)
    playerCol = int(app.px // app.mazeXO)
    if playerRow >= app.dimensions or playerCol >= app.dimensions:
        return False
    if app.maze[playerRow][playerCol] == 'w':
        return False
    return True

def drawPlayer(app, canvas):
    canvas.create_rectangle(app.px-app.playerR, app.py-app.playerR,
                       app.px+app.playerR, app.py+app.playerR,
                       fill='darkGreen')
    canvas.create_line(app.px, app.py, app.px+app.pdx * 5, app.py+app.pdy * 5,
    fill = 'black', width = 2)

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

def checkHorizontal(app, canvas):
    xo, yo, rx, ry, dof = 0, 0, 0, 0, 0
    ra = app.pa     
    aTan = -1/math.tan(ra)
    #looking up
    if ra > math.pi:
        ry = int(app.py // app.mazeYO) * app.mazeYO
        rx = (app.py - ry) * aTan + app.px
        yo = -app.mazeYO
        xo = -yo * aTan
    #looking down
    if ra < math.pi:
        ry = (int(app.py // app.mazeYO)+1) * app.mazeYO
        rx = (app.py - ry) * aTan + app.px
        yo = app.mazeYO
        xo = -yo * aTan
    if ra == 0 or ra == math.pi:
        rx = app.px
        ry = app.py
        dof = app.dimensions
    while dof < app.dimensions:
        rayRow = int(ry // app.mazeYO)
        rayCol = int(rx // app.mazeXO)
        #looking down
        if ra < math.pi:

            if (rayRow < app.dimensions and rayCol < app.dimensions and rayRow >= 0 
            and rayCol >= 0 and app.maze[rayRow][rayCol]=='w'):
                dof = app.dimensions
    
            else:
                rx += xo
                ry += yo
                dof += 1
        #looking up
        else:
            if (rayRow < app.dimensions and rayCol < app.dimensions and rayRow >= 0 
            and rayCol >= 0 and app.maze[rayRow-1][rayCol]=='w'):
                dof = app.dimensions
                
            else:
                rx += xo
                ry += yo
                dof += 1
    
    canvas.create_line(app.px, app.py, rx, ry, fill = 'blue', width = 5)

def checkVertical(app, canvas):
    xo, yo, rx, ry, dof = 0, 0, 0, 0, 0
    ra = app.pa     
    nTan = -math.tan(ra)
    #looking left
    if ra > math.pi/2 and ra < 3*math.pi/2:
        rx = int(app.px // app.mazeXO) * app.mazeXO
        ry = (app.px - rx) * nTan + app.py
        xo = -app.mazeXO
        yo = -xo * nTan
    #looking right
    if ra < math.pi/2 or ra > 3*math.pi/2:
        rx = (int(app.px // app.mazeXO)+1) * app.mazeXO
        ry = (app.px - rx) * nTan + app.py
        xo = app.mazeXO
        yo = -xo * nTan
    if ra == 0 or ra == math.pi:
        rx = app.px
        ry = app.py
        dof = app.dimensions
    while dof < app.dimensions:
        rayRow = int(ry // app.mazeYO)
        rayCol = int(rx // app.mazeXO)
        #looking left
        if ra > math.pi/2 and ra < 3*math.pi/2:
            if (rayRow < app.dimensions and rayCol < app.dimensions and rayRow >= 0 
            and rayCol >= 0 and app.maze[rayRow][rayCol-1]=='w'):
                dof = app.dimensions
                
            else:
                rx += xo
                ry += yo
                dof += 1
        else:
            if (rayRow < app.dimensions and rayCol < app.dimensions and rayRow >= 0 
            and rayCol >= 0 and app.maze[rayRow][rayCol]=='w'):
                dof = app.dimensions
                
            else:
                rx += xo
                ry += yo
                dof += 1
    canvas.create_line(app.px, app.py, rx, ry, fill = 'red', width = 2)

def drawRays(app, canvas):
    checkHorizontal(app, canvas)
    checkVertical(app, canvas)

def checkHorizontalWalls(app, canvas):
    xo, yo, rx, ry, dof = 0, 0, 0, 0, 0
    ra = app.pa      

    if ra == 0 or ra == math.pi:
        ry = app.py
        rx = app.px
        dof = app.dimensions
    #looking Down
    elif ra < math.pi:
        ry = ((int(app.py // app.mazeYO))+1) * app.mazeYO
        if ra < math.pi/2:
            xo = (ry - app.py)/(math.tan(ra))
        elif ra == math.pi/2:
            xo = 0
        else:
            xo = ((app.py - ry)*math.tan(ra-(math.pi/2)))
        rx = (xo + app.px)
        yo = app.mazeYO
    #looking Up
    else:
        ry = int(app.py // app.mazeYO) * app.mazeYO
        if ra < (3*math.pi/2):
            xo = (ry - app.py)/(math.tan(ra-(math.pi)))
        elif ra == (3*math.pi/2):
            xo = 0
        else:
            xo = ((app.py-ry) * (math.tan(ra-(3*math.pi/2))))
        rx = (xo + app.px)
        yo = -app.mazeYO
    
    while dof < app.dimensions:
        rayRow = int(ry // app.mazeYO)
        rayCol = int(rx // app.mazeXO)
        if ra > math.pi:
            if (rayRow < app.dimensions and rayCol < app.dimensions and 
            app.maze[rayRow-1][rayCol] == 'w'):
                dof = app.dimensions
                
            else:
                rx += xo
                ry += yo
                dof += 1
        else:
            if (rayRow < app.dimensions and rayCol < app.dimensions and 
            app.maze[rayRow][rayCol] == 'w'):
                dof = app.dimensions
            else:
                rx += xo
                ry += yo
                dof += 1
    canvas.create_line(app.px, app.py, rx, ry, fill = 'blue', width = 3)

def checkVerticalWalls(app, canvas):
    xo, yo, rx, ry, dof = 0, 0, 0, 0, 0
    ra = app.pa
    #looking Right
    if ra < math.pi/2 or ra > (3 * math.pi/2):
        rx = (int(app.px // app.mazeXO)+1) * app.mazeXO
        if ra == 0:
            yo = 0
        elif ra < math.pi/2:
            yo = (rx - app.px)/(math.tan(ra))
        else:
            yo = (app.px - rx)/(math.tan(ra-(3*math.pi/2)))
        ry = (yo + app.py)
        xo = app.mazeXO
        
    #looking Left
    if ra > math.pi/2 or ra < (3 * math.pi/2):
        rx = (int(app.px // app.mazeXO)) * app.mazeXO
        if ra == math.pi:
            yo = 0
        elif ra < math.pi:
            yo = (app.px - rx)/(math.tan(ra-math.pi/2))
        else:
            yo = (rx-app.px)*(math.tan(ra-math.pi))

        ry = (yo + app.py)
        xo = -app.mazeXO

    if ra == math.pi/2 or ra == 3* math.pi/2:
        ry = app.py
        rx = app.px
        dof = app.dimensions
    
    while dof < app.dimensions:
        rayRow = int(ry // app.mazeYO)
        rayCol = int(rx // app.mazeXO)

        if (rayRow < app.dimensions and rayCol < app.dimensions and 
        app.maze[rayRow][rayCol] == 'w'):
            dof = app.dimensions
        else:
            rx += xo
            ry += yo
            dof += 1
    
    canvas.create_line(app.px, app.py, rx, ry, fill = 'green', width = 1)

def redrawAll(app, canvas):
    drawMaze(app, canvas)
    drawPlayer(app, canvas)
    drawRays(app, canvas)

runApp(width=800, height=800)




