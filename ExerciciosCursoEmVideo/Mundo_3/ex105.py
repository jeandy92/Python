def notas(*notas, sit):
    tamanho = len(notas)
    maior = menor = notas[0]
    soma = 0
    aluno = dict()
    for n in range(0, tamanho):
        if maior < notas[n]:
            maior = notas[n]
        if menor > notas[n]:
            menor = notas[n]
        soma = soma + notas[n]

    media = soma / tamanho

    aluno["Total"] = tamanho
    aluno["Maior"] = maior
    aluno["Menor"] = menor
    aluno["Media"] = media

    if sit:
        if media > 7:
            aluno["Situação"] = "BOA"
        elif media < 5:
            aluno["Situação"] = "RUIM"
        elif 5 <= media <= 7:
            aluno["Situação"] = "RAZOÁVEL"
    return aluno


print(notas(3.5, 2, 6.5, 2, 7, 4, sit=False))
