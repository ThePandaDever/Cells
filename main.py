import pygame as pg
from Types import *
from Cell import *
from Organism import *
import sys,time

pg.init()

ctx = Context(pg.display.set_mode((800,600),pg.RESIZABLE,pg.DOUBLEBUF))
CameraPos = (0,0)
CameraSize = .1

TexturesPaths = {
    "app:icon": "textures/cells/core.png",

    "cell:core": "textures/cells/core.png",
    "cell:movement": "textures/cells/movement.png"
}

Textures = {}
def Update():
    scale = (ctx.screen_size[0]*ctx.screen_ratiob*CameraSize,ctx.screen_size[1]*CameraSize)
    for k in TexturesPaths.keys():
        Textures[k] = pg.transform.scale(pg.image.load(TexturesPaths[k]),scale)

def Add(vec1,vec2):
    return vec1[0]+vec2[0],vec1[1]+vec2[1]
def Sub(vec1,vec2):
    return vec1[0]-vec2[0],vec1[1]-vec2[1]
def Mul(vec1,vec2):
    return vec1[0]*vec2[0],vec1[1]*vec2[1]
def Rotate(val,rot):
    return val[0] * math.sin(math.radians(rot)) + val[1] * math.cos(math.radians(rot)), val[0] * math.cos(math.radians(rot)) + val[1] * math.sin(math.radians(rot))

def SceneToScreen(pos):
    Pos = Mul(Sub(pos,CameraPos),Mul(ctx.screen_size,(CameraSize,CameraSize)))
    Pos = Pos[0] * ctx.screen_ratiob, -Pos[1]
    return Add(Pos,Mul(ctx.screen_size,(.5,.5)))

def Draw(texture:pg.Surface,pos:tuple,rot=None):
    if not rot:
        ctx.screen.blit(texture, Sub(SceneToScreen(pos),Mul(texture.get_size(),(.5,.5))))
    else:
        t = pg.transform.rotate(texture,math.radians(rot))
        ctx.screen.blit(pg.transform.rotate(t,rot), Sub(SceneToScreen(pos), Mul(t.get_size(), (.5, .5))))

Update()

pg.display.set_icon(Textures["app:icon"])
pg.display.set_caption("Cell game")

ctx.scene.organisms.append(Organism(cells=[
    Cell("core",Position=(0,0),AngularVelocity=10),
    Cell("movement",LocalPosition=(-1,-1)),
    Cell("movement",LocalPosition=(1,-1))
],target=
    Cell("movement",LocalPosition=(0,2))
))

LastTime = time.time()
DeltaTime = 0

Clock = pg.time.Clock()

while True:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            pg.quit()
            sys.exit("quit.")
        if e.type == pg.WINDOWRESIZED:
            ctx.update()
            Update()

    ctx.screen.fill((0,3,31))

    for organism in ctx.scene.organisms:
        organism.update(ctx)
        for cell in organism.cells:
            Draw(Textures[f"cell:{cell.Type}"],cell.Position,rot=cell.Rotation)
            cell.update(ctx)
            pg.draw.circle(ctx.screen,(255,255,255),SceneToScreen(Rotate(cell.LocalPosition, cell.ParentOrganism.cells[0].Rotation)),5)

    DeltaTime = time.time() - LastTime
    LastTime = time.time()
    ctx.deltatime = DeltaTime
    pg.display.flip()
    Clock.tick(60)