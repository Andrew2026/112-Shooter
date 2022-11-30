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

def appStarted(app):

    maze = [[1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1],
            [1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1], 
            [1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1], 
            [1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1], 
            [1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1], 
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1], 
            [1, 1, 1, 0, 0, 2, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1], 
            [1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1], 
            [1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1], 
            [1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1], 
            [1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1], 
            [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1], 
            [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1], 
            [1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1], 
            [1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1], 
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 1, 1, 0, 1], 
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
    app.maze = maze
    app.dimensions = len(app.maze)
    app.cellSize = 40
    app.mazeXO = app.width/2 // app.dimensions
    app.mazeYO = app.height // app.dimensions
    app.px = 150
    app.py = 150
    app.pdx = 0
    app.pdy = 0
    app.pa = 1.05
    app.playerR = 5

def keyPressed(app, event):
    #move
    if (event.key == 'Left'):
        app.px += 5
        if not isLegal(app):
            app.px += 5
    if (event.key == 'Right'):
        app.px -= 5
        if not isLegal(app):
            app.px -= 5
    if (event.key == 'Up'):
        app.py += 5
        if not isLegal(app):
            app.py += 5
    if (event.key == 'Down'):
        app.py -= 5
        if not isLegal(app):
            app.py -= 5

    #look around and move at angle
    if (event.key == 'a'):
        app.pa -= 0.1
        if app.pa < 0:
            app.pa += 2 * math.pi
        app.pdx = math.cos(app.pa) * 5
        app.pdy = math.sin(app.pa) * 5

    if (event.key == 'd'):
        app.pa += 0.1
        if app.pa > 2 * math.pi:
            app.pa -= 2 * math.pi
        app.pdx = math.cos(app.pa) * 5
        app.pdy = math.sin(app.pa) * 5

    if (event.key == 'w'):
        app.px += app.pdx
        app.py += app.pdy
        if not isLegal(app):
            app.px -= app.pdx
            app.py -= app.pdy

    if (event.key == 's'):
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

                if app.maze[i][j] != 0:
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
    if ra > 2*math.pi:
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
                    if app.maze[rayVRow][rayVCol-1] == 2:
                        color = 'red'
                    if app.maze[rayVRow][rayVCol-1] == 1:
                        color = 'green'
            else:
                if (rayVRow < app.dimensions and rayVCol < app.dimensions and 
                rayVRow >= 0 and rayVCol >= 0):
                    if app.maze[rayVRow][rayVCol] == 2:
                        color = 'red'
                    if app.maze[rayVRow][rayVCol] == 1:
                        color = 'green'


        elif distV == 0:
            canvas.create_line(app.px, app.py, xH, yH, fill = 'green', 
            width = 1)
            sDist = distH
            #diff color for diff wall
            if ra < math.pi:
                if (rayHRow < app.dimensions and rayHCol < app.dimensions and 
                rayHRow >= 0 and rayHCol >= 0):
                    if app.maze[rayHRow][rayHCol] == 2:
                        color = 'red3'
                    if app.maze[rayHRow][rayHCol] == 1:
                        color = 'green3'
            else:
                if (rayHRow < app.dimensions and rayHCol < app.dimensions and 
                rayHRow >= 0 and rayHCol >= 0):
                    if app.maze[rayHRow-1][rayHCol] == 2:
                        color = 'red3'
                    if app.maze[rayHRow-1][rayHCol] == 1:
                        color = 'green3'

        elif distH > distV:
            canvas.create_line(app.px, app.py, xV, yV, fill = 'green', 
            width = 1)
            sDist = distV
            #diff color for diff wall
            if ra > math.pi/2 and ra < 3*math.pi/2:
                if (rayVRow < app.dimensions and rayVCol < app.dimensions and 
                rayVRow >= 0 and rayVCol >= 0):
                    if app.maze[rayVRow][rayVCol-1] == 2:
                        color = 'red'
                    if app.maze[rayVRow][rayVCol-1] == 1:
                        color = 'green'
            else:
                if (rayVRow < app.dimensions and rayVCol < app.dimensions and 
                rayVRow >= 0 and rayVCol >= 0):
                    if app.maze[rayVRow][rayVCol] == 2:
                        color = 'red'
                    if app.maze[rayVRow][rayVCol] == 1:
                        color = 'green'

        else:
            canvas.create_line(app.px, app.py, xH, yH, fill = 'green', 
            width = 1)
            sDist = distH
            #diff color for diff wall
            if ra < math.pi:
                if (rayHRow < app.dimensions and rayHCol < app.dimensions and 
                rayHRow >= 0 and rayHCol >= 0):
                    if app.maze[rayHRow][rayHCol] == 2:
                        color = 'red3'
                    if app.maze[rayHRow][rayHCol] == 1:
                        color = 'green3'
            else:
                if (rayHRow < app.dimensions and rayHCol < app.dimensions and 
                rayHRow >= 0 and rayHCol >= 0):
                    if app.maze[rayHRow-1][rayHCol] == 2:
                        color = 'red3'
                    if app.maze[rayHRow-1][rayHCol] == 1:
                        color = 'green3'

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

def redrawAll(app, canvas):
    drawBackground(app,canvas)
    drawMaze(app, canvas)
    drawPlayer(app, canvas)
    drawRays(app, canvas)

runApp(width = 1600, height = 800)












