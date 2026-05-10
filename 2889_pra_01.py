# 24/04/26
# autor: lesly michell lopez ramirez
# no. control: 25212889
# grupo c

#%% ejercicio 1
class personaje:
    def __init__(self, nombre, nivel=1, vida=100, ataque=10, defensa=5):
        self.nombre = nombre
        self.nivel = nivel
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa

    def mostrar_stats(self):
        print(f"\n{self.nombre} (nivel {self.nivel})")
        print(f"vida: {self.vida} | Ataque: {self.ataque} | defensa: {self.defensa}")

    def subir_nivel(self):
        self.nivel += 1
        self.vida += 20
        self.ataque += 5
        self.defensa += 3
        print(f"{self.nombre} subio al nivel {self.nivel}.")

    def recibir_daño(self, daño):
        resistencia = self.defensa
        daño_final = max(daño - resistencia, 0)
        self.vida -= daño_final
        print(f"{self.nombre} recibe {daño_final} de daño "
              f"vida restante: {self.vida if self.vida > 0 else 0}")

    def calcular_poder(self):
        raise NotImplementedError("debe implementarse en las clases derivadas ")

    def atacar(self, objetivo):
        daño = self.calcular_poder()
        print(f"{self.nombre} ataca a {objetivo.nombre} con {daño} de daño base ")
        objetivo.recibir_daño(daño)

class Guerrero(personaje):
    def __init__(self, nombre, fuerza_extra=10, armadura=5):
        super().__init__(nombre, vida=120)
        self.fuerza_extra = fuerza_extra
        self.armadura = armadura

    def calcular_poder(self):
        return self.ataque + self.fuerza_extra

    def grito_guerra(self):
        print(f"{self.nombre} lanza un grito de guerra")

    def bloquear(self):
        self.defensa += 5
        print(f"{self.nombre} se concentra en bloquear. defensa: {self.defensa}")

    def afilar_arma(self):
        self.ataque += 5
        print(f"{self.nombre} afila su arma. ataque: {self.ataque}")

class Mago(personaje):
    def __init__(self, nombre, mana=100, inteligencia=8):
        super().__init__(nombre, vida=80, ataque=15)
        self.mana = mana
        self.inteligencia = inteligencia

    def calcular_poder(self):
        return self.ataque + self.inteligencia

    def meditar(self):
        self.mana += 20
        print(f"{self.nombre} medita. Maná: {self.mana}")

    def teletransportar(self):
        if self.mana >= 30:
            self.mana -= 30
            print(f"{self.nombre} se teletransporta!")
        else:
            print(f"{self.nombre} no tiene maná suficiente.")

    def estudiar_runas(self):
        self.ataque += 3
        self.mana += 10
        print(f"{self.nombre} estudia runas. "
              f"Ataque: {self.ataque}, Maná: {self.mana}")

class Arquero(personaje):
    def __init__(self, nombre, precision=10, flechas=20):
        super().__init__(nombre, ataque=12)
        self.precision = precision
        self.flechas = flechas

    def calcular_poder(self):
        return self.ataque + self.precision

    def fuego_rapido(self):
        if self.flechas >= 5:
            self.flechas -= 5
            daño = self.calcular_poder() * 0.5
            print(f"{self.nombre} dispara 5 flechas rapidas "
                  f"({daño:.1f} de daño cada una).")
        else:
            print(f"{self.nombre} no tiene flechas suficientes.")

    def esconderse(self):
        self.defensa += self.precision
        print(f"{self.nombre} se esconde. defensa: {self.defensa}")

    def recolectar_flechas(self):
        self.flechas += 10
        print(f"{self.nombre} recolecta flechas. total: {self.flechas}")

if __name__ == "__main__":
    guerrero = Guerrero("aragorn")
    mago = Mago("gandalf")
    arquero = Arquero("legolas")

    guerrero.mostrar_stats()
    mago.mostrar_stats()
    arquero.mostrar_stats()

    guerrero.atacar(mago)
    arquero.atacar(guerrero)
    mago.atacar(arquero)

    guerrero.subir_nivel()
    mago.meditar()
    mago.teletransportar()
    arquero.esconderse()
    arquero.recolectar_flechas()

    print("\nEstado final:")
    guerrero.mostrar_stats()
    mago.mostrar_stats()
    arquero.mostrar_stats()

#%%ejercicio 2
class Dispositivo:
    def __init__(self, marca, modelo, potencia_watts, bateria_capacidad, precio):
        self.marca = marca
        self.modelo = modelo
        self.potencia_watts = potencia_watts
        self.bateria_capacidad = bateria_capacidad
        self.precio = precio

    def encender(self): 
        print(f"{self.modelo} encendido")

    def apagar(self): 
        print(f"{self.modelo} apagado")

    def mostrar_especs(self):
        print("\nDispositivo:")
        print("Marca:", self.marca)
        print("Modelo:", self.modelo)
        print("Potencia:", self.potencia_watts, "W")
        print("Batería:", self.bateria_capacidad)
        print("Precio:", self.precio)

    def calcular_consumo(self, horas):
        return self.potencia_watts * horas / 1000  # kWh

    def descuento(self, porcentaje):
        return self.precio * (1 - porcentaje / 100)

class Smartphone(Dispositivo):
    def __init__(self, marca, modelo, potencia, bateria, precio, brillo_nits, apps_activas):
        super().__init__(marca, modelo, potencia, bateria, precio)
        self.brillo_nits = brillo_nits
        self.apps_activas = apps_activas

    def calcular_consumo(self, horas):
        return super().calcular_consumo(horas) + self.apps_activas * 0.05 * horas

    def tomar_foto(self): 
        print("Foto tomada")

    def llamar(self): 
        print("Llamando...")

    def enviar_msj(self): 
        print("Mensaje enviado")

class Laptop(Dispositivo):
    def __init__(self, marca, modelo, potencia, bateria, precio, ram_gb, cpu_uso_pct):
        super().__init__(marca, modelo, potencia, bateria, precio)
        self.ram_gb = ram_gb
        self.cpu_uso_pct = cpu_uso_pct

    def calcular_consumo(self, horas):
        return super().calcular_consumo(horas) + self.cpu_uso_pct * 0.1 * horas

    def compilar_codigo(self): 
        print("Compilando...")

    def renderizar(self): 
        print("Renderizando...")

    def limpiar_ram(self): 
        print("RAM limpiada")

class Televisor(Dispositivo):
    def __init__(self, marca, modelo, potencia, bateria, precio, pulgadas, resolucion):
        super().__init__(marca, modelo, potencia, bateria, precio)
        self.pulgadas = pulgadas
        self.resolucion = resolucion

    def calcular_consumo(self, horas):
        return super().calcular_consumo(horas) + self.pulgadas * 0.02 * horas

    def cambiar_canal(self, canal): 
        print(f"Canal cambiado a {canal}")

    def ajustar_brillo(self, valor): 
        print(f"Brillo ajustado a {valor}")

    def configurar_wifi(self, red): 
        print(f"Conectado a {red}")

cel = Smartphone("Apple", "iPhone 15", 20, 3349, 19999, 1000, 1.8)
lap = Laptop("Apple", "MacBook Air M3", 35, 5200, 28999, 16, 512)
tv = Televisor("Samsung", 'Crystal UHD 55"', 145, 0, 13999, 55, "4K")

cel.mostrar_especs()
print("Consumo:", cel.calcular_consumo(5))
print("Precio con descuento:", cel.descuento(10))

lap.mostrar_especs()
print("Consumo:", lap.calcular_consumo(5))
print("Precio con descuento:", lap.descuento(15))

tv.mostrar_especs()
print("Consumo:", tv.calcular_consumo(5))
print("Precio con descuento:", tv.descuento(20))

class Contenido:
    def __init__(self, titulo, año, calificacion, idioma, precio_licencia):
        self.titulo = titulo
        self.año = año
        self.calificacion = calificacion
        self.idioma = idioma
        self.precio_licencia = precio_licencia

    def reproducir(self): 
        print("Reproduciendo", self.titulo)

    def pausar(self): 
        print("Pausado")

    def mostrar_trailer(self): 
        print("Mostrando trailer")

    def mostrar_datos(self):
        print("\nContenido:")
        print("Titulo:", self.titulo)
        print("Año:", self.año)
        print("Calificacion:", self.calificacion)
        print("Idioma:", self.idioma)
        print("Precio base:", self.precio_licencia)

    def calcular_precio_final(self):
        return self.precio_licencia * 1.16

    def dar_reseña(self, puntos):
        self.calificacion = (self.calificacion + puntos) / 2

class Pelicula(Contenido):
    def __init__(self, titulo, año, calificacion, idioma, precio, duracion_min, director):
        super().__init__(titulo, año, calificacion, idioma, precio)
        self.duracion_min = duracion_min
        self.director = director

    def mostrar_datos(self):
        super().mostrar_datos()
        print("Duracion:", self.duracion_min, "min")
        print("Director:", self.director)

    def calcular_precio_final(self):
        return super().calcular_precio_final() + self.duracion_min * 0.1

    def ver_escenas_post_creditos(self): 
        print("Escena post-creditos")

    def cambiar_subtitulos(self): 
        print("Subtitulos cambiados")

    def descargar(self): 
        print("Pelicula descargada")

class Serie(Contenido):
    def __init__(self, titulo, año, calificacion, idioma, precio, temporadas, episodios):
        super().__init__(titulo, año, calificacion, idioma, precio)
        self.temporadas = temporadas
        self.episodios = episodios

    def mostrar_datos(self):
        super().mostrar_datos()
        print("Temporadas:", self.temporadas)
        print("Episodios:", self.episodios)

    def calcular_precio_final(self):
        return super().calcular_precio_final() + self.episodios * 5

    def marcar_visto(self): 
        print("Marcado como visto")

    def siguiente_ep(self): 
        print("Siguiente episodio")

    def resumen_anterior(self): 
        print("Resumen mostrado")

class Documental(Contenido):
    def __init__(self, titulo, año, calificacion, idioma, precio, tema_educativo, narrador):
        super().__init__(titulo, año, calificacion, idioma, precio)
        self.tema_educativo = tema_educativo
        self.narrador = narrador

    def mostrar_datos(self):
        super().mostrar_datos()
        print("Tema:", self.tema_educativo)
        print("Narrador:", self.narrador)

    def calcular_precio_final(self):
        return super().calcular_precio_final() + 50

    def descargar_guia(self): 
        print("Guia descargada")

    def ver_bibliografia(self): 
        print("Bibliografia mostrada")

    def entrevistar_experto(self): 
        print("Entrevista disponible")

p = Pelicula("La tumba de las luciernagas", 1988, 9.5, "Japones", 89, 88, "Isao Takahata")
s = Serie("Weak Hero Class 1", 2022, 8.9, "Coreano", 320, 2, 8)
d = Documental("Mi maestro el pulpo", 2020, 9.1, "Ingles", 85, "Naturaleza", "Pippa Ehrlich")

p.mostrar_datos()
print("Precio final:", p.calcular_precio_final())

s.mostrar_datos()
print("Precio final:", s.calcular_precio_final())

d.mostrar_datos()
print("Precio final:", d.calcular_precio_final())

#%% ejercicio 3
class Empleado:
    def __init__(self, nombre, id_empleado, sueldo_base, antiguedad, faltas=0):
        self.nombre = nombre
        self.id_empleado = id_empleado
        self.sueldo_base = sueldo_base
        self.antiguedad = antiguedad
        self.faltas = faltas

    def mostrar_datos(self):
        print(f"\n{self.nombre} (ID: {self.id_empleado})")
        print(f"Sueldo base: ${self.sueldo_base} | "
              f"Antiguedad: {self.antiguedad} años | Faltas: {self.faltas}")

    def registrar_falta(self):
        self.faltas += 1
        print(f"Se registró una falta para {self.nombre}. Total: {self.faltas} faltas.")

    def calcular_vacaciones(self):
        dias = min(self.antiguedad * 15, 90)
        print(f"{self.nombre} tiene {dias} dias de vacaciones anuales.")
        return dias

    def bono_antiguedad(self):
        return self.sueldo_base * (self.antiguedad * 0.01)

    def calcular_neto(self):
        bono = self.bono_antiguedad()
        descuento = 0.10 * (self.sueldo_base + bono)
        neto = self.sueldo_base + bono - descuento
        print(f"Sueldo neto de {self.nombre}: ${neto:.2f}")
        return neto

class Cajero(Empleado):
    def __init__(self, nombre, id_empleado, sueldo_base, antiguedad,
                 arqueos_exito=0, riesgo_caja=0.02):
        super().__init__(nombre, id_empleado, sueldo_base, antiguedad)
        self.arqueos_exito = arqueos_exito
        self.riesgo_caja = riesgo_caja

    def validar_efectivo(self):
        self.arqueos_exito += 1
        print(f"{self.nombre} valido efectivo correctamente. "
              f"Arqueos exitosos: {self.arqueos_exito}")

    def cerrar_turno(self):
        print(f"{self.nombre} cerro turno. Caja cerrada.")

    def reportar_sobrante(self, cantidad):
        print(f"{self.nombre} reporta un sobrante de ${cantidad} en la caja.")

    def calcular_neto(self):
        bono_arqueos = self.sueldo_base * (self.arqueos_exito * 0.01)
        bono = self.bono_antiguedad() + bono_arqueos
        descuento = 0.10 * (self.sueldo_base + bono)
        neto = self.sueldo_base + bono - descuento
        print(f"Sueldo neto de {self.nombre} (Cajero): ${neto:.2f}")
        return neto

class Asesor(Empleado):
    def __init__(self, nombre, id_empleado, sueldo_base, antiguedad,
                 ventas_seguro=0, comision_venta=0.05):
        super().__init__(nombre, id_empleado, sueldo_base, antiguedad)
        self.ventas_seguro = ventas_seguro
        self.comision_venta = comision_venta

    def contactar_cliente(self, cliente):
        print(f"{self.nombre} contacta al cliente: {cliente}")

    def cotizar_seguro(self, monto):
        comision = monto * self.comision_venta
        self.ventas_seguro += comision
        print(f"Se cotizo un seguro por ${monto}. Comision: ${comision:.2f}")

    def enviar_poliza(self):
        print(f"{self.nombre} envia la poliza al cliente.")

    def calcular_neto(self):
        bono = self.bono_antiguedad() + self.ventas_seguro
        descuento = 0.10 * (self.sueldo_base + bono)
        neto = self.sueldo_base + bono - descuento
        print(f"Sueldo neto de {self.nombre} (Asesor): ${neto:.2f}")
        return neto

class Gerente(Empleado):
    def __init__(self, nombre, id_empleado, sueldo_base, antiguedad,
                 metas_logradas=0, presupuesto_area=0):
        super().__init__(nombre, id_empleado, sueldo_base, antiguedad)
        self.metas_logradas = metas_logradas
        self.presupuesto_area = presupuesto_area

    def aprobar_gasto(self, monto):
        if monto <= self.presupuesto_area:
            self.presupuesto_area -= monto
            print(f"{self.nombre} aprueba un gasto de ${monto}. "
                  f"Presupuesto restante: ${self.presupuesto_area}")
        else:
            print(f"{self.nombre} no puede aprobar gasto, presupuesto insuficiente.")

    def evaluar_equipo(self):
        print(f"{self.nombre} evalua el desempeño del equipo.")

    def planear_trimestre(self):
        self.metas_logradas += 1
        print(f"{self.nombre} planea el trimestre. Metas logradas: {self.metas_logradas}")

    def calcular_neto(self):
        bono_metas = self.sueldo_base * (self.metas_logradas * 0.05)
        bono = self.bono_antiguedad() + bono_metas
        descuento = 0.10 * (self.sueldo_base + bono)
        neto = self.sueldo_base + bono - descuento
        print(f"Sueldo neto de {self.nombre} (Gerente): ${neto:.2f}")
        return neto

if __name__ == "__main__":
    cajero = Cajero("asiul", 101, 3000, 3, arqueos_exito=5)
    asesor = Asesor("alejandra", 102, 3500, 4, ventas_seguro=1000)
    gerente = Gerente("alexa", 103, 5000, 6, metas_logradas=3, presupuesto_area=10000)

    cajero.mostrar_datos()
    asesor.mostrar_datos()
    gerente.mostrar_datos()

    cajero.calcular_vacaciones()
    asesor.calcular_vacaciones()
    gerente.calcular_vacaciones()

    cajero.validar_efectivo()
    cajero.cerrar_turno()
    cajero.calcular_neto()

    asesor.contactar_cliente("Sr. Landon")
    asesor.cotizar_seguro(2000)
    asesor.calcular_neto()

    gerente.aprobar_gasto(2500)
    gerente.evaluar_equipo()
    gerente.planear_trimestre()
    gerente.calcular_neto()

