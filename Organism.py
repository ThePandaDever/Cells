import math,importlib

def Add(vec1,vec2):
    return vec1[0]+vec2[0],vec1[1]+vec2[1]
def Sub(vec1,vec2):
    return vec1[0]-vec2[0],vec1[1]-vec2[1]
def Mul(vec1,vec2):
    return vec1[0]*vec2[0],vec1[1]*vec2[1]
def Div(vec1,vec2):
    return vec1[0]/vec2[0],vec1[1]/vec2[1]
def Rotate(val,rot):
    return val[0] * math.sin(math.radians(rot)) + val[1] * math.cos(math.radians(rot)), val[1] * math.sin(math.radians(rot)) + val[0] * math.cos(math.radians(rot))

class Organism:
    cells: list
    def __init__(self, cells=None, target = None):
        if cells is None:
            cells = []
        self.cells = cells
        self.target = target
    def update(self,ctx):
        for cell in self.cells:
            cell.ParentOrganism = self
            if cell.Type == "movement":
                self.cells[0].Velocity = Mul(Sub(self.cells[0].Position,self.target.Position),(.1,.1))