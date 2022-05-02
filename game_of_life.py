ACTIVE_COLOUR = (0,155,0)
class Node:
    x:int
    y:int
    size:int
    _x:int
    _y:int
    colour: tuple[int,int,int]
    def __init__(self, _x, _y, size)->None:
        self.x = _x*size
        self.y = _y*size
        self.size = size
        self._x = _x
        self._y = _y
        self.colour = (255,255,255)
    def isAlive(self) -> bool:
        return self.colour == ACTIVE_COLOUR
    def born(self) -> None:
        self.colour = ACTIVE_COLOUR
    def die(self) -> None:
        self.colour = (255,255,255)
    def __iter__(self):
        return iter(self.x, self.y, self.colour)