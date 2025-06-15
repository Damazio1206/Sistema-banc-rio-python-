class Usuario:
    def __init__(self, nome, nascimento, cpf, endereco):
        self.nome = nome
        self.nascimento = nascimento
        self.cpf = cpf
        self.endereco = endereco

    def __str__(self):
        return f"{self.nome} ({self.cpf})"
