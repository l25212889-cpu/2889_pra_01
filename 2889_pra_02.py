# 24/04/26
# autor: lesly michell lopez ramirez
# no. control: 25212889
# grupo c

#%% Ejercicio 1
from abc import ABC, abstractmethod

class albumvinilo(ABC):
    def __init__(self, titulo, artista, anio_lanzamiento, precio, stock):
        self.titulo = titulo
        self.artista = artista
        self.anio_lanzamiento = anio_lanzamiento
        self.precio = precio
        self.stock = stock

    #metodos abstractos
    @abstractmethod
    def reproducir(self):
        pass
    @abstractmethod
    def mostrar_genero(self):
        pass

    #metodos concretos
    def mostrar_info(self):
        print(f"titulo: {self.titulo}")
        print(f"artista: {self.artista}")
        print(f"año de lanzamiento: {self.anio_lanzamiento}")
        print(f"precio: ${self.precio:.2f}")

    def aplicar_descuento(self, porcentaje):
        precio_original = self.precio
        self.precio -= self.precio * (porcentaje / 100)

        print(f"precio original: ${precio_original:.2f}")
        print(f"precio con descuento: ${self.precio:.2f}")

    def estado_stock(self):
        if self.stock > 0:
            print(f"disponible. quedan {self.stock} unidades en stock.")
        else:
            print("agotado.")

#clase derivada: R&B
class AlbumRNB(albumvinilo):
    def __init__(self, titulo, artista, anio_lanzamiento, precio, stock,
                 colaboraciones, nivel_soul):
        super().__init__(titulo, artista, anio_lanzamiento, precio, stock)
        self.colaboraciones = colaboraciones
        self.nivel_soul = nivel_soul

    #metodos sobrescritos
    def reproducir(self):
        print(f"reproduciendo '{self.titulo}' con suaves ritmos de R&B.")

    def mostrar_genero(self):
        print("genero: R&B")

    # Métodos propios
    def sesion_nocturna(self):
        print(f"{self.titulo} crea el ambiente perfecto para la noche.")

    def improvisar_vocal(self):
        print(f"{self.artista} realiza una impresionante improvisacion vocal.")

    def mezclar_ritmos(self):
        print("fusionando ritmos soul y R&B contemporaneo.")


#clase derivada: K-Pop
class AlbumKpop(albumvinilo):
    def __init__(self, titulo, artista, anio_lanzamiento, precio, stock,
                 grupo, num_photocards):
        super().__init__(titulo, artista, anio_lanzamiento, precio, stock)
        self.grupo = grupo
        self.num_photocards = num_photocards

    #metodos sobrescritos
    def reproducir(self):
        print(f"reproduciendo '{self.titulo}' con gran energía K-Pop.")

    def mostrar_genero(self):
        print("genero: K-Pop")

    #metodos propios
    def mostrar_photocards(self):
        print(f"este album incluye {self.num_photocards} photocards.")

    def fan_chant(self):
        print(f"los fans realizan el fan chant de {self.grupo}.")

    def version_coleccionista(self):
        print("edicion especial para coleccionistas disponible.")


# Clase derivada: Rap
class AlbumRap(albumvinilo):
    def __init__(self, titulo, artista, anio_lanzamiento, precio, stock,
                 num_tracks, certificacion):
        super().__init__(titulo, artista, anio_lanzamiento, precio, stock)
        self.num_tracks = num_tracks
        self.certificacion = certificacion

    # Métodos sobrescritos
    def reproducir(self):
        print(f"reproduciendo '{self.titulo}' con potentes barras de rap.")

    def mostrar_genero(self):
        print("genero: Rap")

    # Métodos propios
    def freestyle(self):
        print(f"{self.artista} improvisa unas barras impresionantes.")

    def batalla_rap(self):
        print(f"{self.artista} domina la batalla de rap.")

    def ganar_grammy(self):
        print(f"'{self.titulo}' obtuvo certificación {self.certificacion}.")


album1 = AlbumRNB("SOS", "SZA", 2022, 799.99, 10, 5, 9)
album2 = AlbumKpop("Born Pink", "BLACKPINK", 2022, 899.99, 15, "BLACKPINK", 8)
album3 = AlbumRap("To Pimp a Butterfly", "Kendrick Lamar", 2015,
                  949.99, 12, 16, "Platino")

coleccion = [album1, album2, album3]

for album in coleccion:
    print("\n" + "=" * 40)
    album.mostrar_info()
    album.mostrar_genero()
    album.reproducir()
    album.estado_stock()