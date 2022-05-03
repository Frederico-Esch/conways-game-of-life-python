ACTIVE_COLOUR = (0,155,0)
class Node:
    x:int
    y:int
    size:int
    _x:int
    _y:int

    colour: dict[int, tuple[int,int,int]]

    def __init__(self, _x, _y, size)->None:
        self.x = _x*size
        self.y = _y*size
        self.size = size
        self._x = _x
        self._y = _y
        self.colour = {
            True: (255,255,255),
            False: (255,255,255)
        }

    def isAlive(self, state:bool) -> bool:
        return self.colour[state] == ACTIVE_COLOUR
    def born(self, state:bool) -> None:
        self.colour[state] = ACTIVE_COLOUR
    def die(self, state:bool) -> None:
        self.colour[state] = (255,255,255)
    def __iter__(self):
        return iter(self.x, self.y, self.colour)