from vpython import *
import time, math, random

# Set up the values I will need

fJato = 32.e6         # Thrust force (assume constant for now) in Newtons
dt = 1                  # timestep in seconds
m = 2.0e6               # mass in kilograms

Ntimesteps = 100        # total number of timesteps for the simulation

oxa=50000               # For plotting, the wireframe dimensions along Cartesian axes
oya=50000
oza=50000

g = 9.8                 # acceleration of gravity--constant at first for a flat Earth
                        
v_yo = 0.               # initial speed along y axis--zero at launch
v_xo = 0.               # later maybe we will make it 2D!
v_zo = 0.               # or even 3D!

x_o = 0                 # initial value of x, y and z--starts at the origin
y_o = 0
z_o = 0

# create wireframe with dimensions of the pixel sizes along x,y,z for now 
square1 = curve(pos=[(oxa,oya,oza),(-oxa,oya,oza),(-oxa,-oya,oza),(oxa,-oya,oza),(oxa,oya,oza)])
square2 = curve(pos=[(oxa,oya,-oza),(-oxa,oya,-oza),(-oxa,-oya,-oza),(oxa,-oya,-oza),(oxa,oya,-oza)])
square3 = curve(pos=[(oxa,oya,oza),(oxa,oya,-oza),(oxa,-oya,-oza),(oxa,-oya,oza),(oxa,oya,oza)])
square4 = curve(pos=[(-oxa,oya,oza),(-oxa,oya,-oza),(-oxa,-oya,-oza),(-oxa,-oya,oza),(-oxa,oya,oza)])
# end of wireframe

rocket = cone (pos=vector(x_o,y_o,z_o), radius=1000, axis=vector(0,5000,0), color=color.white)     # initialize rocket's position at (xo,yo,zo), pointing along +y
rocket.velocity = vector(v_xo,v_yo,v_zo)                                # initialize rocket's velocity too                        

rocket_position=[]
rocket_speed=[]

c = curve(pos=(x_o,y_o,z_o),color=color.red)            # plots the rocket's trajectory

n=0

while n <= Ntimesteps:
    rate (20)                                         # screen refresh rate           
    
    ascend = fJato - m*g 
    
    rocket_force = vector(0.,ascend,0.)        # at first we ignore the loss of mass from fuel ejection

    rocket.velocity = rocket.velocity + (rocket_force/m)*dt 
    rocket.pos = rocket.pos + rocket.velocity*dt        #   first update velocity, then update position second!

    rocket_position.append(mag(rocket.pos))
    rocket_speed.append(mag(rocket.velocity))
    c.append(pos=rocket.pos)
    n=n+1
    


# a canned functional plotting program from the vpython manual--use to plot distance and speed vs. time



#scene2=display() # new screen with the plots

funct1 = gcurve(color=color.cyan) 
funct2 = gcurve(delta=0.05, color=color.yellow)


n=0

while n < Ntimesteps:
    funct1.plot(pos=(n*dt,rocket_position[n]))      #  rocket altitude vs. time
    funct2.plot(pos=(n*dt,40.*rocket_speed[n]))     #  rocket speed vs. time--scaled to be on same plot as position
    n=n+1
