class Encaixe:
    def __init__(self, data, consulta_1_id=None, consulta_2_id=None, consulta_3_id=None, id=None):
        self.id = id
        self.consulta_1_id = consulta_1_id
        self.consulta_2_id = consulta_2_id
        self.consulta_3_id = consulta_3_id
        self.data = data

    def limite(self):
        return (self.consulta_1_id is not None and
                self.consulta_2_id is not None and
                self.consulta_3_id is not None
                )

    def __str__(self):
        return f'id: {self.id}\nconsulta_1_id : {self.consulta_1_id}\nconsulta_2_id : {self.consulta_2_id}' \
               f'\nconsulta_3_id : {self.consulta_3_id}\ndata_hora: {self.data}'

    def get_json(self):
        return {
            'id': self.id,
            'consulta_1_id': self.consulta_1_id,
            'consulta_2_id': self.consulta_2_id,
            'consulta_3_id': self.consulta_3_id,
            'data_hora': self.data
        }
