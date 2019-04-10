pessoa = dict()
pessoas = list()
somaidade = 0
media = 0

nome = str(input('NOME: '))
sexo = str(input('SEXO: [M/F]'))
while sexo not in 'fFmM':
    sexo = str(input('Erro! por favor, digite novamente SEXO: [M/F]'))
idade = int(input('IDADE: '))

pessoa['nome'] = nome
pessoa['sexo'] = sexo
pessoa['idade'] = idade
somaidade = somaidade + idade

pessoas.append(pessoa.copy())

print(pessoas)

while True:

    opcao = str(input("Quer continuar ? [S/N]")).upper()
    while opcao not in 'nNsS':
        opcao = str(input("Quer continuar ? [S/N]")).upper()
    if opcao in 'sS':
        pessoa.clear()

        nome = str(input('NOME: ')).title()
        sexo = str(input('SEXO: [M/F]'))
        while sexo not in 'fFmM':
            sexo = str(input('Erro! por favor, digite novamente SEXO: [M/F]'))
        idade = int(input('IDADE: '))

        pessoa['nome'] = nome
        pessoa['sexo'] = sexo
        pessoa['idade'] = idade

        somaidade = somaidade + idade

        pessoas.append(pessoa.copy())

    if opcao in 'nN':
        break
media = somaidade/len(pessoas)
print("-=" * 30)
print(f"Ao todo temos {len(pessoas)} pessoas cadastradas ")
print(f"A média de idade é de {media:.2f} anos ")
print(f"As mulheres cadastradas foram ", end=' ')
# for  p  in pessoas:
#     if p['sexo'] in 'fF':
#         print(f"{p['nome']}")

for c in range(0, len(pessoas)):
    if pessoas[c]['sexo'] in 'fF':
        print(f"=>{pessoas[c]['nome']}".title())
for c in range(0, len(pessoas)):
    if pessoas[c]['idade'] > media:
        print(f"\nA pessoa {pessoas[c]['nome']} está acima da média")
        print(f"Sua idade {pessoas[c]['idade']} idade da média {media}")
        print(f"Sexo {pessoas[c]['sexo']}")
        print()
