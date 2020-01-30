from vpython import *
import time
import math, random

#Introdução, intruções e escolha do planeta
scene.caption = """És um orbe extraterrestre a tentar aterrar nos planetas do Sistema Solar. \n \nControlos: Propulsor: 'z'; Movimento da nave: W,A,S,D \n"""

#Titulo do começo de jogo e tamanho da tela 
scene.title = "Landing Game \n CUIDADO COM OS VENTOS FORTES! \n Clique na tecla 'P' para começar!"
scene.width = 1000
scene.height = 500
scene.forward = vector(0,-5,-10)
#variaveis
W = 900
H = 500
dt = 0.04
g = -9.8
vel = vector(0,-1,0)
acel = vector(0,g,0)
origin = vector (0,20,0)

#superficie e contrução do orbe com as asas laterais
surface= box (pos=vector(0, 0, 0), size=vector(20, 0.5, 20),  visible=True, texture={'file':textures.earth})
core = sphere(pos=vec(0,10,0), radius=0.9, color=color.red)
p1 = cone(pos=vector(0.9,10,0), size=vector(1,1,1), axis=vec(0,0,0), width=1.2, height =1.2, color=color.white)
p2 = cone(pos=vector(-0.9,10,0), size=vector(1,1,1), axis=vec(-1,0,0), width=1.2, height =1.2, color=color.white )
p3 = cone(pos=vector(0,10,-0.9), size=vector(1,1,1), axis=vec(0,0,-1), width=1.2,  height =1.2, color=color.white )
p4 = cone(pos=vector(0,10,0.9), size=vector(1,1,1), axis=vec(0,0,1),  width=1.2, height =1.2, color=color.white)
orb = compound([core, p1, p2, p3, p4,],  make_trail = False, axis=vector(0,0,0))

#função para a escolha de planeta e atualização da gravidade e textura correspondente a cada um
def M(m):
    global col, surface, g, keyInput, release, origin, grav
    
    surface.visible = False
    val = m.selected
    if val == "Terra": 
        surface.texture = {'file':textures.earth}
        g = -9.8
        orb.pos = origin

    elif val == "Marte": 
        surface.texture = {'file':textures.stucco}
        g = -3.7 
        orb.pos = origin
        
    elif val == "Mercúrio": 
        surface.texture = {'file':textures.rough}
        g = -3.7 
        orb.pos = origin
    elif val == "Vénus": 
        surface.texture = {'file':textures.rock}
        g = -8.9
        orb.pos = origin
    elif val == "Júpiter": 
        surface.texture = "https://i.imgur.com/ls2fKsP.jpg"
        g = -24.8
        orb.pos = origin

    elif val == "Saturno": 
        surface.texture = {'file':textures.stucco}
        g = -10.5 
        orb.pos = origin
        
    elif val == "Urano": 
        surface.texture = {'file':textures.rough}
        g = -8.9
        orb.pos = origin
    elif val == "Neptuno": 
        surface.texture = {'file':textures.rock}
        g = -11.2
        orb.pos = origin
    
    
    surface.visible = True

menu(choices=['Mercúrio', 'Vénus', 'Terra', 'Marte', 'Júpiter', 'Saturno', 'Urano', 'Neptuno'], index=2, bind=M)  

#função para definir a tecla para iniciar a simulação e os controlos do movimento do orbe 
def keyInput(ev):    
    k = ev.key

#tecla do movimento para a direita
    if k == "d" :
        if orb.pos.y - orb.height + 0.5 > 0:
            orb.pos.x += 1     
    
#tecla do movimento para a esquerda
    if k == "a" :
        if orb.pos.y - orb.height + 0.5 > 0:
            orb.pos.x -= 1    
      
        
#tecla do movimento para a frente
    if k == "w" :
        if orb.pos.y - orb.height + 0.5 > 0:
            orb.pos.z -= 1          
        
        
#tecla do movimento para trás
    if k == "s" :
        if orb.pos.y - orb.height + 0.5 > 0:
            orb.pos.z += 1
       
#tecla do propulsor
    if k == "z":
        if orb.pos.y - orb.height + 0.5 > 0:
            orb.pos.y += 1

#tecla para o utilizador iniciar o jogo
    if k == "p":
        if scene.title == "Perdeste-te no vazio! \n \n \n Clica na tecla 'P' para tentares novamente...":
            orb.pos = origin
            scene.title="A Recomeçar dentro de 3segundos...! \n \n \n \n"
            time.sleep(3)
            scene.title="COMEÇOU... \n \n \n \n"
            grav()
        else:
            scene.title="COMEÇOU... \n \n \n \n"
            orb.pos = origin
            time.sleep(1)
            grav()

scene.bind("keydown", keyInput)

#função que aciona a queda do orbe segundo a gravidade de cada planeta
def grav():
    cycle = True 
    vel = vector(0,-1,0)
    acel = vector(0,g,0)
    vel = vel + acel*dt
#ciclo while que faz o orbe cair segundo a gravidade de cada planeta e sobre o orbe atuam ventos laterais que 
# a sua trajetória e dificultam a aterragem na superficie
    while cycle:
        rate (30)
        windX = random.randint(-1, 1)
        windZ = random.randint(-1, 1)
        surface.visible = True
        orb.pos = orb.pos + vel * dt + 0.5 *acel * dt**2 
        orb.pos.x -= windX
        orb.pos.z -= windZ
        #Quando o orbe chega ao chão, é feita a verificação se aterrou no solo, ou no vazio
        if orb.pos.y - orb.height + 0.5 < 0:
            if -10 <= orb.pos.z <= 10 and -10 <= orb.pos.x <= 10:
                vel.y = 0
                acel.y = 0  
                scene.title="Aterrou no solo, Parabéns! \n \n \n Existem novos planetas para descobrir..."
                cycle = False
            else:
                vel.y = 0
                acel.y = 0  
                scene.title="Perdeste-te no vazio! \n \n \n Clica na tecla 'P' para tentares novamente..."
                cycle = False
        #caso ainda nao tenha chegado ao chao, a velocidade de queda do orbe vai aumentando
        else:
            vel = vel + acel*dt