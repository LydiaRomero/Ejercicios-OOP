class NIF():
    def __init__(self,numero):
        self.numero = numero
    def calcular_letra(self):
        lista_letras = ["T","R","W","A","G","M","Y","F","P","D","X","B","N","J","Z","S","Q","V","H","L","C","K","E"]
        resto = self.numero % 23
        resto = int(resto)
        letra = lista_letras[resto]
        return letra
L = NIF(54240737)
R = NIF(54240738)
print(L.calcular_letra())
print(R.calcular_letra())
