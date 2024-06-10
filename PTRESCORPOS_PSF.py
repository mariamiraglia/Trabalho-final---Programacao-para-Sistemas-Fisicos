from math import *
import turtle as tl 

# Criar o corpo celestial

class Corpo_celestial:
    def __init__(self, massa, px, py, vx, vy):
        self.massa = massa  # Em kg
        self.px = px        # Em m
        self.py = py
        self.vx = vx        # Em km/h
        self.vy = vy

# Definir as equações usadas

def Gravidade(m1, m2, r):
        Fg = G * (m1*m2)/(r**2)
        return Fg
    
def Cinematica(px, py, vx, vy, ax, ay):
        px =+ vx * dt + (ax*(dt)**2)/2
        py =+ vy * dt + (ay*(dt)**2)/2
        vx =+ ax * dt 
        vy =+ ay * dt

        return (px, py, vx, vy)

def ponto(nome, x, y, cor, dot_size=3):
      nome.shapesize(dot_size)
      nome.color(cor)
      nome.penup()
      nome.goto(x,y)
      nome.dot(5, cor)


G = 6.67e-11
dt = 0.5
scale= 1000
C1 = Corpo_celestial(6e24, 0, 0, 0, 0)                #6e24
C2 = Corpo_celestial(7.35e22, 6e5, 0, 15e3, 0)         #7.35e22
C3 = Corpo_celestial(6e21, 5e5, -4e5, -5e3, 0)    #6e21 

t1 = tl.Turtle()
t2 = tl.Turtle()
t3 = tl.Turtle()
t1.shape("circle")
t2.shape("circle")
t3.shape("circle")

for i in range(1200):
    # Determinar a distância entre os corpos
    r12 = sqrt((C1.px-C2.px)**2 + (C1.py-C2.py)**2)
    r23 = sqrt((C2.px - C3.px )**2 + (C2.py - C3.py)**2)
    r13 = sqrt((C1.px - C3.px)**2 + (C1.py - C3.py)**2)

    # Determinar a força entre cada par de corpos
    Fg12 = Gravidade(C1.massa, C2.massa, r12)
    Fg23 = Gravidade(C2.massa, C3.massa, r23)
    Fg13 = Gravidade(C1.massa, C3.massa, r13)

    # Decompor as forças em x e y

    Fx12 = Fg12 * (C1.px - C2.px)/r12
    Fy12 = Fg12 * (C1.py - C2.py)/r12
    Fx23 = Fg23 * (C2.px - C3.px)/r23
    Fy23 = Fg23 * (C2.py - C3.py)/r23
    Fx13 = Fg13 * (C1.px - C3.px)/r13
    Fy13 = Fg13 * (C1.py - C3.py)/r13

    # Agora, vamos atualizar as posições e velocidades de acordo com as equações da cinemática
    a1x = (Fx12 + Fx13)/C1.massa
    a1y = (Fy12 + Fy13)/C1.massa
    C1.px, C1.py, C1.vx, C1.py = Cinematica(C1.px, C1.py, C1.vx, C1.vy, a1x, a1y)

    a2x = (Fx12 + Fx23)/C2.massa
    a2y = (Fy12 + Fy23)/C2.massa
    C2.px, C2.py, C2.vx, C2.py = Cinematica(C2.px, C2.py, C2.vx, C2.vy, a2x, a2y)

    a3x = (Fx23 + Fx13)/C3.massa
    a3y = (Fy23 + Fy13)/C3.massa
    C3.px, C3.py, C3.vx, C3.py = Cinematica(C3.px, C3.py, C3.vx, C3.vy, a3x, a3y)

    # Desenhar as novas posições

    ponto(t1, C1.px/scale, C1.py/scale, "blue", C1.massa/6e24)
    ponto(t2, C2.px/scale, C2.py/scale, "gray", C2.massa/6e24)
    ponto(t3, C3.px/scale, C3.py/scale, "red", C3.massa/6e24)



