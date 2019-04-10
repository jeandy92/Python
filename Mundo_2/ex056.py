# nome = ["Joaquim", "Maria", "Creuza", "Manoel"]
# idade = [25, 18, 21, 65]
# sexo = ["M", "F", "F", "M"]
# pessoas = ["",0,""]

media = 0
somaidade =0
velho= 0
nomevelho =''
totmulher = 0

for i in range(1, 5):
     nome = str(input('Nome: ')).strip()
     idade = int(input("Idade: "))
     sexo = str(input("Sexo [F/M]: ")).strip()
     somaidade += idade
     if velho == 0 and sexo in 'Mm':
          velho = idade
          nomevelho = nome
     if idade > velho and sexo in 'Mm':
          velho = idade
          nomevelho = nome
     if sexo in 'Ff' and idade < 20:
          totmulher += 1



print('Média: {}'.format((somaidade/4)))
print('Mais velho: {}'.format({nomevelho}))
print('Mulher com menos de 20: {}'.format({totmulher}))
