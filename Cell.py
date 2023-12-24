from Types import *

def Add(vec1,vec2):
    return vec1[0]+vec2[0],vec1[1]+vec2[1]
def Sub(vec1,vec2):
    return vec1[0]-vec2[0],vec1[1]-vec2[1]
def Mul(vec1,vec2):
    return vec1[0]*vec2[0],vec1[1]*vec2[1]

class Cell:
    Position: tuple
    Rotation: float
    Type: str
    Velocity: tuple
    AngularVelocity: float
    def __init__(self,Type,Position=(0,0),Rotation=0,Velocity=(0,0),AngularVelocity=0):
        self.Position = Position
        self.Rotation = Rotation
        self.Type=Type

        self.Velocity = Velocity
        self.AngularVelocity = AngularVelocity

    def update(self,ctx: Context):
        self.Position = self.Position[0]+self.Velocity[0] * ctx.deltatime, self.Position[1]+self.Velocity[1]*ctx.deltatime
        self.Rotation = self.Rotation + self.AngularVelocity * ctx.deltatime