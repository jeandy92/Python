import emoji
import random

nomeJogador = "joaquim"
jokenpô = ((1, "PEDRA"), (2, "PAPEL"), (3, "TESOURA"))

print("-" * 40)
print("*" * 10, "BEM VINDO {}".format(nomeJogador.upper()), "*" * 10)
print("-" * 10, "'J-O-K-E-N-P-Ô", "-" * 10)
print(emoji.emojize("|  1 - :fist: PEDRA - :hand: 2 - PAPEL - :scissors: 3 - TESOURA  :door: 0 - EXIT   |", use_aliases=True))

escolhaJogador = int(input("R: "))
escolhaMaquina = random.choice(jokenpô)

if escolhaJogador == 0:
    print(emoji.emojize('Até Logo :wave: !!!!'))
elif escolhaJogador == 1 and escolhaMaquina[0] == 1:
    print(emoji.emojize("Empate :open_mouth: !!!!! \n", use_aliases=True))
elif escolhaJogador == 1 and escolhaMaquina[0] == 2:
    print(emoji.emojize("Perdeu :cry: !!!!! \n :fist: PEDRA perde embrulhado pelo :hand: PAPEL \n", use_aliases=True))
elif escolhaJogador == 1 and escolhaMaquina[0] == 3:
    print(emoji.emojize("Ganhou :unamused:  \n :fist: PEDRA esmaga :scissors: TESOURA \n", use_aliases=True))
elif escolhaJogador == 2 and escolhaMaquina[0] == 1:
    print(emoji.emojize("Ganhou :unamused:  \n :fist: PEDRA perde embrulhado pelo :hand: PAPEL \n", use_aliases=True))
elif escolhaJogador == 2 and escolhaMaquina[0] == 2:
    print(emoji.emojize("Empate :open_mouth: !!!!! \n", use_aliases=True))
elif escolhaJogador == 2 and escolhaMaquina[0] == 3:
    print(emoji.emojize("Perdeu :cry: !!!!! \n :scissors: TESOURA fatia papel :hand: PAPEL \n", use_aliases=True))
elif escolhaJogador == 3 and escolhaMaquina[0] == 1:
    print(emoji.emojize("Perdeu :cry: !!!!!  \n :fist: PEDRA esmaga TESOURA :hand: PAPEL \n", use_aliases=True))
elif escolhaJogador == 3 and escolhaMaquina[0] == 2:
    print(emoji.emojize("Ganhou :unamused:  \n :scissors: TESOURA fatia papel :hand: PAPEL \n", use_aliases=True))
elif escolhaJogador == 3 and escolhaMaquina[0] == 3:
    print(emoji.emojize("Empate :open_mouth: !!!!! \n", use_aliases=True))
