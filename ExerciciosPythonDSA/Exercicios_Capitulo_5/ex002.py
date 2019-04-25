# Exercício 2 - Crie uma classe chamada Pessoa() com os atributos: nome, cidade,
# telefone e e-mail. Use pelo menos 2
# métodos especiais na sua classe.
# Crie um objeto da sua classe e faça uma chamada a pelo menos um dos seus métodos
# especiais.


class Pessoa():

    def __init__(self, nome="Não preenchido", cidade="Não preenchido", telefone=0000, email="Não preenchido"):
        self.nome = nome
        self.cidade = cidade
        self.telefone = telefone
        self.email = email
        print("Objeto criado")

    def __str__(self):
        return f" | Nome: {self.nome}\n" \
            f" | Cidade: {self.cidade}\n" \
            f" | Telefone: {self.telefone}\n" \
            f" | E-mail: {self.email}\n"


pessoa1 = Pessoa(nome="Jean", cidade="barueri", telefone=423232, email="jean@ja.com")
pessoa2 = Pessoa()

print(str(pessoa1))
