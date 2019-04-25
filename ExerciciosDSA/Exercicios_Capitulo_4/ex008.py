# Exercício 8 - Considere o código abaixo. Obtenha o mesmo resultado usando o pacote time.
# Não conhece o pacote time? Pesquise!
import datetime
import time

print(datetime.datetime.now().strftime("%d/%m/%Y %H:%M"))
print(time.strftime("%d/%m/%Y %H:%M"))
