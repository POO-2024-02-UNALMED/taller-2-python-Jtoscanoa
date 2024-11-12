class Asiento():
    def init(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, ncolor: str):
        colores = ["rojo", "verde", "amarillo", "negro", "blanco"]
        if ncolor in colores:
            self.color = ncolor
            return True
        else:
            return False
class Motor():
    def init(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro
    def cambiarRegistro(self, nregistro: int):
        self.registro = nregistro
    def asignarTipo(self, ntipo: str):
        if ntipo == "electrico" or ntipo == "electrico":
            self.tipo = ntipo
if __name__ == "__main__":
    class Auto():
        cantidadCreados = 0
        def init(self, modelo, precio, asientos, marca, motor, registro):
            self.modelo= modelo
            self.precio = precio
            self.asientos = asientos
            self.marca = marca
            self.motor = motor
            self.registro = registro
            Auto.cantidadCreados += 1

        def cantidadAsientos(self):
            contador = 0
            if self.asientos != None:
                for Asiento in self.asientos:
                    if Asiento != None:
                        contador += 1
            return contador

        def verificarIntegridad(self):
            if self.motor == None or self.asientos == None:
                return "Las piezas no son originales"
            for Asiento in self.asientos:
                if Asiento is not None and (Asiento.registro != self.registro or self.motor.registro != self.registro):
                    return "Las piezas no son originales"

            return "Auto original"
