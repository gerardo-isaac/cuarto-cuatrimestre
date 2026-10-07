#Programa principal desde la que se manda llamar los objetos de la clase de coches

from coches import Coches, Camiones, Camionetas

coche1 =Coches("VW", "Blanco", "2022", 220, 150, 5)
coche2 =Coches("Nissan", "Azul", "2020", 180, 150, 6)

camion1=Camiones("dina", "negro", 2020, 180, 300, 12, 8, 2500)
camion2=Camiones("star", "blanco", 2019, 150, 200, 14, 6, 2000)

camioneta1=Camionetas("renault", "amarillo", "2025", 240, 250, 8, "delantera", True)
camioneta2=Camionetas("nissan", "blanca", "2020", 180, 150, 6, "tracera", False)

