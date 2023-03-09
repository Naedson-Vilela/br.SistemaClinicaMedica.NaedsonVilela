class PlanoSaude:

    FIELDS_TO_VALIDATE = ['nome', 'limite_consultas']

    def __init__(self, nome, limite_consultas, id=None):
        self.id = id
        self.nome = nome
        self.limite_consultas = limite_consultas

    def __str__(self):
        return f'id: {self.id}\nnome: {self.nome}\nlimite_consultas: {self.limite_consultas}'

    def get_json(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'limite_consultas': self.limite_consultas
        }
