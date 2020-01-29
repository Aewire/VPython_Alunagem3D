from vpython import *
import time
import math, random


#butoes de controlo do orb
    #espaço = propulsor
    #setas = orientacao da cabeça do orb

scene.caption = """Fodeu."""


scene.title = "Landing Game"
scene.width = 1000
scene.height = 500
scene.forward = vector(0,-5,-10)
#valores
W = 900
H = 500
randAxis= random.randint(1, 3)
dt = 0.01
g = -9.8
fJet = 10
vel = vector(0,0,0)
acel = vector(0,g,0)
origin = vector (0,10,0)

surface= box (pos=vector(0, 0, 0), size=vector(20, 0.5, 20),  visible=True, texture={'file':textures.earth})
core = sphere(pos=vec(0,10,0), radius=0.9, color=color.red)
p1 = cone(pos=vector(0.9,10,0), size=vector(1,1,1), axis=vec(0,0,0), width=1.2, height =1.2, color=color.white)
p2 = cone(pos=vector(-0.9,10,0), size=vector(1,1,1), axis=vec(-1,0,0), width=1.2, height =1.2, color=color.white )
p3 = cone(pos=vector(0,10,-0.9), size=vector(1,1,1), axis=vec(0,0,-1), width=1.2,  height =1.2, color=color.white )
p4 = cone(pos=vector(0,10,0.9), size=vector(1,1,1), axis=vec(0,0,1),  width=1.2, height =1.2, color=color.white)

orb = compound([core, p1, p2, p3, p4,],  make_trail = False, axis=vector(0,0,0))

cycle = True 
#scene.range = 5

#scene.camera.follow(orb)
def M(m):
    global col, surface, cycle, g, keyInput, release, origin  
    
    
    surface.visible = False
    val = m.selected
    if val == "earth": 
        surface.texture = {'file':textures.earth}
        g = -9.8
        orb.pos = origin
        cycle = True
    elif val == "mars": 
        surface.texture = {'file':textures.stucco}
        g = -8.2 
        orb.pos = origin
        cycle = True
        print(orb.pos.y - orb.height + 0.5)
        print(cycle)
        
    elif val == "mercury": 
        surface.texture = {'file':textures.rough}
        g = -4.8 
        orb.pos = origin
        cycle = True
    elif val == "venus": 
        surface.texture = {'file':textures.rock}
        g = -6
        orb.pos = origin
        cycle = True
    
    surface.visible = True

menu(choices=['Choose a planet', 'earth', 'mars', 'mercury', 'venus'], index=0, bind=M)  

############################
def keyInput(ev):    
    k = ev.key
    #label( pos=vec(0,0,5), text="k = " + k)
    #print(" k = " , k)
    if k == "d" :
        acel.x += 2.5     
    
    if k == "a" :
        acel.x -= 2.5     
      
        
    if k == "w" :
        acel.z -= 2.5          
        
        
    if k == "s" :
        acel.z += 2.5
        

    if k == "z" :        
        acel.y += 30 - g* dt
    

def release(ev):   
      
    acel.y += g
    if acel.y >= 30:
        acel.y = 30

scene.bind("keydown", keyInput)
scene.bind("keyup", release)

print(orb.pos.y - orb.height + 0.5)

while cycle and orb.pos.y - orb.height + 0.5 >= 0: 
    rate (30) 
    acel.y += g   
    vel = vel + acel * dt
    orb.pos = orb.pos + vel * dt + 0.5 *acel * dt**2    
    
    
    if orb.pos.y - orb.height + 0.5 <= 0:     
        acel.y = 0    
        
    else:
        acel.y = 0   
           





#[textures.flower, textures.granite, textures.gravel, textures.metal, textures.rock, textures.rough,
      #textures.rug, textures.stones, textures.stucco, textures.wood, textures.wood_old, textures.earth]


