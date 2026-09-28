from collections.abc import dict_items

from disciplina import Disciplina

class Aluno:
    def __init__(self, nome, matricula, curso):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
        self.disciplinas = []
        self.notas_por_disciplina = {}

    # Adiciona disciplina AO aluno
    def matricular(self, disciplina: Disciplina):
        if disciplina not in self.disciplinas:
            self.disciplinas.append(disciplina)
        self.notas_por_disciplina.setdefault(disciplina.nome, [])

    def adicionar_nota(self, disciplina: Disciplina, nota: float):
        # Adicionar uma nota do aluno naquela disciplina
        self.notas_por_disciplina[disciplina.nome].append(nota)

    def media_por_disciplina(self, disciplina: Disciplina) -> float:
        notas = self.notas_por_disciplina.get(disciplina.nome, [])
        if not notas:
            return 0.0
        return sum(notas) / len(notas)

    def media_geral(self) -> float:
        medias_disciplinas = []
        for disciplina in self.disciplinas:
            media = self.media_por_disciplina(disciplina)
            medias_disciplinas.append(media)
        return sum(medias_disciplinas) / len(medias_disciplinas)

    def exibir_boletim(self):
        print(f"\nAluno: {self.nome}, Matrícula: {self.matricula}")
        print(f"Curso: {self.curso}")

        if not self.disciplinas:
            print("Sem disciplinas matriculadas.")
            return

        for d in self.disciplinas:
            notas = self.notas_por_disciplina.get(d.nome, [])
            media_d = self.media_por_disciplina(d)

            d.exibir_infos()
            print(f"Notas do aluno em: {d.nome}: {notas}")
            print(f"Média do aluno em: {d.nome}: {media_d}")

            print(f"Média Geral: (self.media_geral()}")