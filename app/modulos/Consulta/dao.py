from app.modulos.Consulta.model import Consulta
from app.database.connect import ConnectDataBase
from app.modulos.Paciente.dao import DaoPaciente
from app.modulos.Consulta.sql import SQLConsulta


class DaoConsulta:
    def __init__(self):
        self.base_dados = ConnectDataBase().get_instance()

    def salvar(self, consulta):
        if consulta is None:
            return None
        cursor = self.base_dados.cursor()
        cursor.execute(SQLConsulta._SCRIPT_INSERT.format(SQLConsulta._NOME_TABELA, consulta.data_hora,
                                                         consulta.revisao, consulta.paciente_id))
        id = cursor.fetchone()[0]
        self.base_dados.commit()
        cursor.close()
        consulta.id = id
        return consulta

    def get_all(self):
        consultas = []
        cursor = self.base_dados.cursor()
        sql = SQLConsulta._SCRIPT_SELECT_ALL
        cursor.execute(sql)
        consultas_query = cursor.fetchall()
        columns_name = [desc[0] for desc in cursor.description]
        for consulta in consultas_query:
            data = dict(zip(columns_name, consulta))
            consultas.append(Consulta(**data))
        if consultas:
            return consultas
        else:
            return None

    def get_by_id(self, id):
        if id is None:
            return None
        cursor = self.base_dados.cursor()
        cursor.execute(SQLConsulta._SCRIPT_SELECT_BY_ID.format(SQLConsulta._NOME_TABELA, id))
        consulta = cursor.fetchone()
        if not consulta:
            return None
        columns_name = [desc[0] for desc in cursor.description]
        data = dict(zip(columns_name, consulta))
        consulta = Consulta(**data)
        cursor.close()
        return consulta

    def get_by_paciente_id(self, id):
        paciente = DaoPaciente().get_by_id(id)
        if paciente:
            consultas = []
            cursor = self.base_dados.cursor()
            cursor.execute(SQLConsulta._SCRIPT_SELECT_BY_PACIENTE_ID.format(SQLConsulta._NOME_TABELA, paciente.id))
            consultas_query = cursor.fetchall()
            columns_name = [desc[0] for desc in cursor.description]
            for consulta in consultas_query:
                data = dict(zip(columns_name, consulta))
                consultas.append(Consulta(**data))
            if consultas:
                return consultas
            else:
                return None
        return None

    def update(self, consulta_old, consulta_new):
        cursor = self.base_dados.cursor()
        cursor.execute(SQLConsulta._SCRIPT_UPDATE.format(SQLConsulta._NOME_TABELA, consulta_new.data_hora,
                                                         consulta_new.revisao,
                                                         consulta_new.paciente_id,
                                                         consulta_old.id))
        self.base_dados.commit()
        cursor.close()

    def delete(self, id):
        cursor = self.base_dados.cursor()
        cursor.execute(SQLConsulta._SCRIPT_DELETE.format(SQLConsulta._NOME_TABELA, id))
        self.base_dados.commit()
        cursor.close()
