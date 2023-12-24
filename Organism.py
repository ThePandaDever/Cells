from Cell import Cell

def Add(vec1,vec2):
    return vec1[0]+vec2[0],vec1[1]+vec2[1]
def Sub(vec1,vec2):
    return vec1[0]-vec2[0],vec1[1]-vec2[1]
def Mul(vec1,vec2):
    return vec1[0]*vec2[0],vec1[1]*vec2[1]
def Div(vec1,vec2):
    return vec1[0]/vec2[0],vec1[1]/vec2[1]

class Organism:
    cells: list
    target: Cell
    def __init__(self, cells=None, target = None):
        if cells is None:
            cells = []
        self.cells = cells
        self.target = target
    def update(self):
        cells_movement = []
        for cell in self.cells:
            if self.target:
                if cell.Type == "movement":
                    cells_movement.append(cell)
        movement_pivot = cells_movement[0].Position
        for cell_movement in cells_movement:
            if cell_movement != cells_movement[0]:
                movement_pivot = Add(movement_pivot,Div(Sub(cell_movement.Position,movement_pivot),(len(cells_movement),len(cells_movement))))
        self.movement_pivot = movement_pivot