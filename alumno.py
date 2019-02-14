class Alumno():
    def __init__(self, matricula, nombre, nota1, nota2, nota3):
        self.matricula = matricula
        self.nombre = nombre
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
    def calcular_media(self):
        media = (self.nota1 + self.nota2 + self.nota3) / 3
        if media >= 4.8:
            nota_final = "aprobado"
        else:
            nota_final = "suspenso"
        return media, nota_final
        
L = Alumno(231, "Lydia", 4, 4, 4)
print("El alumno",L.nombre, "con número de matrícula", L.matricula, "tiene una media de", L.calcular_media())
