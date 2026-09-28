from aluno import Aluno
from disciplina import Disciplina

# CRIAR 1 aluno

aluno1 = Aluno("Jandiroba", "123456", "CC")

prompt_ia = Disciplina("IA", "Jorge")
DSA = Disciplina("DSA", "Álvaro")

# Matricular aluno nas 2 disciplinas (Vincular objeto aluno as duas disciplinas)

aluno1.matricular(prompt_ia)
aluno1.matricular(DSA)

# Adicionar notas do aluno em cada disciplina

aluno1.adicionar_nota(prompt_ia, 10)
aluno1.adicionar_nota(prompt_ia, 6)
aluno1.adicionar_nota(DSA, 8)
aluno1.adicionar_nota(DSA, 9)

notas_ia = aluno1.media_por_disciplina(prompt_ia)
print(notas_ia)

print(aluno1.media_geral())
