from app.database.connect import ConnectDataBase
from app.modulos.Encaixe.sql import SQLEncaixe
from app.modulos.Encaixe.model import Encaixe
from app.modulos.Consulta.dao import DaoConsulta


class DaoEncaixe:
    def __init__(self):
        self.data_base = ConnectDataBase().get_instance()


    def salvar(self, data):
        cursor = self.data_base.cursor()
        if data is None:
            return None
        cursor.execute(SQLEncaixe._SCRIPT_INSERT.format(data))
        self.data_base.commit()
        id = cursor.fetchone()[0]
        encaixe = Encaixe(data, id=id)
        cursor.close()
        return encaixe

    def save_consulta(self, consulta):
        if consulta is None:
            return None
        with self.data_base.cursor() as cursor:
            encaixe = self.get_by_data(consulta.data_hora)
            print(encaixe)
            if encaixe and encaixe.limite():
                return False

            if not encaixe:
                encaixe = self.salvar(consulta.data_hora)

            if DaoConsulta().get_by_id(consulta.id) is None:
                consulta = DaoConsulta().salvar(consulta)
            else:
                return None

            if encaixe.consulta_1_id is None:
                cursor.execute(SQLEncaixe._SCRIPTS_UPDATE_CONSULTA.format('consulta_1_id',
                                                                          consulta.id, consulta.data_hora))
                self.data_base.commit()
                return self.get_by_data(consulta.data_hora)
            elif encaixe.consulta_2_id is None:
                cursor.execute(SQLEncaixe._SCRIPTS_UPDATE_CONSULTA.format('consulta_2_id',
                                                                          consulta.id, consulta.data_hora))
                self.data_base.commit()
                return self.get_by_data(consulta.data_hora)
            elif encaixe.consulta_3_id is None:
                cursor.execute(SQLEncaixe._SCRIPTS_UPDATE_CONSULTA.format('consulta_3_id',
                                                                          consulta.id, consulta.data_hora))
                self.data_base.commit()
                return self.get_by_data(consulta.data_hora)
            return True

    def get_all(self):
        encaixes = []
        cursor = self.data_base.cursor()
        sql = SQLEncaixe._SCRIPT_SELECT_ALL
        cursor.execute(sql)
        encaixes_query = cursor.fetchall()
        columns_name = [desc[0] for desc in cursor.description]
        for encaixe in encaixes_query:
            data = dict(zip(columns_name, encaixe))
            encaixes.append(Encaixe(**data))
        if encaixes:
            return encaixes
        else:
            return None

    def get_by_id(self, id):
        if id is None:
            return None
        cursor = self.data_base.cursor()
        cursor.execute(SQLEncaixe._SCRIPT_SELECT_BY_ID.format(SQLEncaixe._NOME_TABELA, id))
        encaixe = cursor.fetchone()
        if not encaixe:
            return None
        columns_name = [desc[0] for desc in cursor.description]
        data = dict(zip(columns_name, encaixe))
        encaixe = Encaixe(**data)
        cursor.close()
        return encaixe

    def get_by_data(self, data):
        if data is None:
            return None
        cursor = self.data_base.cursor()
        cursor.execute(SQLEncaixe._SCRIPTS_GET_BY_DATA.format(data))
        encaixe = cursor.fetchone()
        if not encaixe:
            return None
        columns_name = [desc[0] for desc in cursor.description]
        content = dict(zip(columns_name, encaixe))
        encaixe = Encaixe(**content)
        return encaixe

    def get_consulta_id(self, id, value):
        cursor = self.data_base.cursor()
        cursor.execute(SQLEncaixe._SCRIPT_GET_CONSULTA_ID.format(value, SQLEncaixe._NOME_TABELA, id))
        consulta_id = cursor.fetchone()[0]
        cursor.close()
        return consulta_id

    def remarcar_consulta(self, id, value, data):
        cursor = self.data_base.cursor()
        cursor.execute(SQLEncaixe._SCRIPT_GET_CONSULTA_ID.format(value, SQLEncaixe._NOME_TABELA, id))
        consulta_id = cursor.fetchone()[0]

        consulta = DaoConsulta().get_by_id(consulta_id)
        consulta.data_hora = data
        consulta.id = None

        self.save_consulta(consulta)
        self.delete_consulta_marcada(id, value)
        cursor.close()
        return consulta_id

    def delete_consulta_marcada(self, id, value):
        cursor = self.data_base.cursor()
        cursor.execute(SQLEncaixe._SCRIPT_GET_CONSULTA_ID.format(value, SQLEncaixe._NOME_TABELA, id))
        consulta_id = cursor.fetchone()[0]
        cursor.execute(SQLEncaixe._SCRIPT_DELETE_CONSULTA_MARCADA.format(SQLEncaixe._NOME_TABELA, value, id))
        self.data_base.commit()
        cursor.close()
        return consulta_id

    def delete(self, id):
        cursor = self.data_base.cursor()
        cursor.execute(SQLEncaixe._SCRIPT_DELETE.format(SQLEncaixe._NOME_TABELA, id))
        self.data_base.commit()
        cursor.close()
