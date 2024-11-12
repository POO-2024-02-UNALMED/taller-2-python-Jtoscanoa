class Asiento:
    def __init__(self, color: str, precio: float, registro: int):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, nuevo_color: str) -> bool:
        colores = ["rojo", "verde", "amarillo", "negro", "blanco"]
        if nuevo_color in colores:
            self.color = nuevo_color
            return True
        else:
            return False

class Motor:
    def __init__(self, numero_cilindros: int, tipo: str, registro: int):
        self.numeroCilindros = numero_cilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, nuevo_registro: int):
        self.registro = nuevo_registro

    def asignarTipo(self, nuevo_tipo: str):
        if nuevo_tipo in ["electrico", "combustion"]:
            self.tipo = nuevo_tipo

if __name__ == "__main__":
    class Auto:
        cantidadCreados = 0

        def __init__(self, modelo: str, precio: float, asientos: list, marca: str, motor: Motor, registro: int):
            self.modelo = modelo
            self.precio = precio
            self.asientos = asientos
            self.marca = marca
            self.motor = motor
            self.registro = registro
            Auto.cantidadCreados += 1

        def cantidadAsientos(self) -> int:
            contador = 0
            if self.asientos is not None:
                for asiento in self.asientos:
                    if asiento is not None:
                        contador += 1
            return contador

        def verificarIntegridad(self) -> str:
            if self.motor is None or self.asientos is None:
                return "Las piezas no son originales"
            for asiento in self.asientos:
                if asiento is not None and (asiento.registro != self.registro or self.motor.registro != self.registro):
                    return "Las piezas no son originales"

            return "Auto original"
