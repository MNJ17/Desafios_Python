from carro import Carro
from moto import Moto

fusca = Carro("Fusca", "Amarelo", 1980)
gol = Carro("Gol", "Prata", 2021)
honda_neo = Moto("Honda Neo", "Preto", 2022)
kawasaki = Moto("Kawasaki Ninja", "Verde", 2000)

print(fusca)
print(fusca.buzinar())
print(fusca.abrir_porta_malas())
fusca.dirigir()
fusca.dirigir()
print(f"{fusca.hodometro} km rodados")
print(gol)
print(gol.buzinar())
print(gol.abrir_porta_malas())
print(honda_neo)
print(honda_neo.buzinar())
print(kawasaki)
print(kawasaki.buzinar())
kawasaki.pilotar()
kawasaki.pilotar()
print(f"{kawasaki.hodometro} km rodados")
