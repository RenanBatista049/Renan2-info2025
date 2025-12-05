class Aula():

    def __init__(self, titulo):
        self.titulo = titulo

    def imprime(self):
        print("Foi inserida uma nova aula", self.titulo)

aula = Aula("Revisão Python")
aula.imprime()