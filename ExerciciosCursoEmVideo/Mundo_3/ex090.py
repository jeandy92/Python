aluno = dict()
aluno['nome'] = str(input("NOME: "))
aluno['media'] = float(input(f"MEDIA DO {aluno['nome']}: ".upper()))

if aluno['media'] > 7:
    aluno['situacao'] = 'APROVADO'
else:
    aluno['situacao'] = 'REPROVADO'

for k,v in aluno.items():
    print(f"{k} é igual a {v} ".upper())

