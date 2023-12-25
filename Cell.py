from Types import *
from Organism import Organism
import math
def Add(vec1,vec2):
    return vec1[0]+vec2[0],vec1[1]+vec2[1]
def Sub(vec1,vec2):
    return vec1[0]-vec2[0],vec1[1]-vec2[1]
def Mul(vec1,vec2):
    return vec1[0]*vec2[0],vec1[1]*vec2[1]
def Rotate(val,rot):
    radians = math.radians(rot)
    x,y = val
    xx = x * math.cos(radians) + y * math.sin(radians)
    yy = -x * math.sin(radians) + y * math.cos(radians)
    return xx,yy
class Cell:
    Position: tuple
    LocalPosition: tuple
    Rotation: float
    Type: str
    Velocity: tuple
    AngularVelocity: float
    ParentOrganism: Organism
    def __init__(self,Type,Position=(0,0),Rotation=0,Velocity=(0,0),AngularVelocity=0,LocalPosition = (0,0),ParentOrganism=Organism()):
        self.Position = Position
        self.LocalPosition = LocalPosition
        self.Rotation = Rotation
        self.Type=Type
        self.ParentOrganism = ParentOrganism

        self.Velocity = Velocity
        self.AngularVelocity = AngularVelocity

    def update(self,ctx: Context):
        self.Velocity = Add(self.Velocity,Mul(Sub(Add(self.ParentOrganism.cells[0].Position,Rotate(self.LocalPosition,self.ParentOrganism.cells[0].Rotation)),self.Position),(ctx.deltatime*10,ctx.deltatime*10)))
        self.AngularVelocity = self.AngularVelocity + (self.ParentOrganism.cells[0].Rotation - self.Rotation) * ctx.deltatime*10
        self.Position = self.Position[0]+self.Velocity[0] * ctx.deltatime, self.Position[1]+self.Velocity[1]*ctx.deltatime
        self.Rotation = self.Rotation + self.AngularVelocity * ctx.deltatime