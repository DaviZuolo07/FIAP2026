class Disciplina:
    def __init__(self, nome, professor):
        self.nome = nome
        self.professor = professor
    def exibir_infos(self):
        print(f"Disciplina: {self.nome}, professor: {self.professor}")

# python = Disciplina("PCP", "Prof. Russi")
# python.exibir_infos()