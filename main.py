import pygame as pg
from game_of_life import Node

MOUSE_RELEASED = False
SIZE = 600
size = 10
amount = SIZE//size

last_mouse = (-1, -1)
neighbours_loc = (
    ( 1,  0),
    ( 1,  1),
    ( 0,  1),
    (-1,  1),
    (-1,  0),
    (-1, -1),
    ( 0, -1),
    ( 1, -1)
)
iterate = False

pg.init() 

screen = pg.display.set_mode((SIZE, SIZE))
grid = [[Node(i,j,size) for i in range(amount)] for j in range(amount)]

def reset_grid():
    for row in grid:
        for node in row:
            node.die()

def mouse_click() -> None:
    global MOUSE_RELEASED
    global last_mouse

    y,x = pg.mouse.get_pos()
    buttons = pg.mouse.get_pressed()
    if(not any(buttons)):
        MOUSE_RELEASED = False
        last_mouse = (-1, -1)
        return
    elif buttons[2] :
        reset_grid()
        return 
    x //= size
    y //= size
    if(last_mouse != (x,y)):
        #print(x,y)
        node = grid[x][y]
        if not node.isAlive():
            node.born()
        else:
            node.die()
        last_mouse = (x,y)

def pool_events() -> None:
    global MOUSE_RELEASED
    global iterate

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit(0)
        elif (event.type == pg.MOUSEBUTTONDOWN or MOUSE_RELEASED) and not iterate:
            MOUSE_RELEASED = True
            mouse_click()
        elif event.type == pg.KEYDOWN:
            #print(pg.key.get_pressed())
            if(pg.key.get_pressed()[pg.K_SPACE]):
                iterate = not iterate

while True:
    pool_events()

    screen.fill((150,150,150))

    for rows in grid:
        for node in rows:
            #x, y, colour = rect
            pg.draw.rect(screen, node.colour, (node.x, node.y, size-2, size-2))

            if iterate:
                _x = node._x
                _y = node._y
                n_neighbours = 0
                for neigh in neighbours_loc:
                    nx = _x + neigh[0]
                    ny = _y + neigh[1]
                    if nx >= 0 and nx < amount and ny >= 0 and ny < amount:
                        if grid[ny][nx].isAlive():
                            n_neighbours+=1
                if n_neighbours == 3:
                    grid[_y][_x].born()
                elif n_neighbours < 2 or n_neighbours > 3:
                    grid[_y][_x].die()
    pg.display.update()