# Exercício 9 - Considere os dois dicionários abaixo.
# Crie um terceiro dicionário com as chaves do dicionário 1 e os valores do dicionário 2.
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 4, 'd': 5}

dict3 = dict(zip(dict1.keys(), dict2.values()))
print(dict1)
print(dict2)
print(dict3)
