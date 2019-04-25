alunos = list()
nomes = list()
notas = list()

nome = str(input("Nome: ")).upper()
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
media = (nota1 + nota2) / 2
alunos.append([nome, [nota1, nota2, media]])

while True:
    opcao = str(input("Deseja continuar [S/N]")).upper()
    while opcao not in 'SN':
        opcao = str(input("Deseja continuar [S/N]")).upper()
    if opcao == 'S':
        nome = str(input("Nome: ")).upper()
        nota1 = float(input("Nota 1: "))
        nota2 = float(input("Nota 2: "))
        media = (nota1 + nota2) / 2
        alunos.append([nome, [nota1, nota2, media]])
    if opcao == 'N':
        break
print("=-" * 30)
print(" " * 10 + "BOLETIM ESCOLAR" + " " * 10)
print("=-" * 30)
print("NOME" + " " * 20 + "MEDIA")
for p in alunos:
    media = p[1]
    print(f"{p[0]}", end='')
    print(" " * 20, end=' ')
    print(f"{media[-1]}", end='')
    print()
while True:
    busca = str(input("\n Mostrar a nota de qual aluno ? 99 para o programa \n")).upper()
    for p in alunos:
        if p[0] in busca:
            print("!!! Aluno Encontrado !!!".center(20))
            notas = p[1]
            print(f"Suas Notas foram:\n {notas[0]}  ,  {notas[1]}")
    if busca == "99":
        break
