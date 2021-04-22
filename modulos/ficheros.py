class Fichero:
    def __init__(self, nombre):
        self.nombre = nombre

    def write(self, texto):
        fichero = open(self.nombre, 'wt')
        fichero.write(texto)
        fichero.close()

    def append(self, texto):
        fichero = open(self.nombre, 'at')
        fichero.write(texto)
        fichero.close()

    def read(self):
        fichero = open(self.nombre, 'rt')
        texto = fichero.read()
        return texto