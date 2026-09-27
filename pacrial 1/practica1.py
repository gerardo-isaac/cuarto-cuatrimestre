"""
 Practica # 1 Implementar ejercicio el paradigma estructurado VS OO

 Elaborar un programa que calcule el area de un rectangulo
"""

print("\033c")

#Implementar el paradigma estructurado
 print("\033c")
class Coches:
    marca=""
    color=" Blanco"
    modelo=""
    velocidad=100
    potencia=0
    asientos=0 

    def acelerar(self):
        self.velocidad+=1
        print(f"Ahora la velocidad final es :{self.velocidad}")
        
    def frenar(self):
        self.velocidad-=1
        print(f"Ahora la velocidad final es :{self.velocidad}")



#Implementar el paradigma Orientado a Objetos (OO)

