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