class Consulta:

    FIELDS_TO_VALIDATE = ['data_hora', 'revisao', 'paciente_id']

    def __init__(self, data_hora, revisao, paciente_id, id=None):
        self.id = id
        self.data_hora = data_hora
        self.revisao = revisao
        self.paciente_id = paciente_id

    def __str__(self):
        return f'id: {self.id}\ndata_hora: {self.data_hora}\nrevisao: {self.revisao}\npaciente_id: {self.paciente_id}'

    def get_json(self):
        return {
            'id': self.id,
            'data_hora': self.data_hora,
            'revisao': self.revisao,
            'paciente_id': self.paciente_id
        }
