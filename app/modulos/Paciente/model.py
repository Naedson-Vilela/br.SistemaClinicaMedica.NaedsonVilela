import datetime


class Paciente:

    FIELDS_TO_VALIDATE = ['nome', 'endereco', 'telefone', 'email', 'data_nascimento']

    def __init__(self, nome, endereco, telefone, email, data_nascimento, plano_saude_id, data_primeira_consulta=None, id=None):
        self.id = id
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.email = email
        self.data_nascimento = data_nascimento
        self.plano_saude_id = plano_saude_id
        self.data_primeira_consulta = data_primeira_consulta

    def __str__(self):
        return f'id: {self.id}\nnome: {self.nome}\nendereco: {self.endereco}\ntelefone: {self.telefone} ' \
               f'\nemail:{self.email}\ndata_nascimento: {self.data_nascimento}' \
               f'\ndata_primeira_consulta: {self.data_primeira_consulta}' \
               f'\nplano_saude: {self.plano_saude_id}'

    def get_json(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'endereco': self.endereco,
            'telefone': self.telefone,
            'email': self.email,
            'data_nascimento': self.data_nascimento.strftime('%d/%m/%y'),
            'plano_saude_id': self.plano_saude_id,
            'data_primeira_consulta': self.data_primeira_consulta,
        }
