from app.database.connect import ConnectDataBase
from app.modulos.Paciente.model import Paciente
from app.modulos.Paciente.sql import SQLPaciente


class DaoPaciente:

    def __init__(self) -> None:
        self.data_base = ConnectDataBase().get_instance()

    def salvar(self, paciente):
        if paciente is not None:
            cursor = self.data_base.cursor()
            cursor.execute(SQLPaciente._SCRIPT_INSERT, (paciente.nome, paciente.endereco, paciente.email,
                                                        paciente.telefone, paciente.data_nascimento,
                                                        str(paciente.plano_saude_id)))
            id = cursor.fetchone()[0]
            self.data_base.commit()
            cursor.close()
            paciente.id = id
            return paciente
        else:
            raise Exception('Erro ao cadastrar paciente')


    def get_all(self, busca=None):
        pacientes = []
        cursor = self.data_base.cursor()
        sql = SQLPaciente._SCRIPT_SELECT_BUSCA.format(SQLPaciente._NOME_TABELA, busca)\
            if busca else SQLPaciente._SCRIPT_SELECT_ALL
        cursor.execute(sql)
        all_pacientes = cursor.fetchall()
        columns_name = [desc[0] for desc in cursor.description]
        for paciente_query in all_pacientes:
            data = dict(zip(columns_name, paciente_query))
            pacientes.append(Paciente(**data))
        if pacientes:
            return pacientes
        else:
            raise Exception('Não foi possivel recuperar os dados')


    def get_by_id(self, id):
        cursor = self.data_base.cursor()
        cursor.execute(SQLPaciente._SCRIPT_SELECT_BY_ID.format(SQLPaciente._NOME_TABELA, id))
        paciente = cursor.fetchone()
        if not paciente:
            return None
        collumn_name = [desc[0] for desc in cursor.description]
        data = dict(zip(collumn_name, paciente))
        paciente = Paciente(**data)
        cursor.close()
        return paciente

    def get_by_plano_saude_id(self, plano_saude_id):
        cursor = self.data_base.cursor()
        cursor.execute(SQLPaciente._SCRIPT_SELECT_BY_PLANO_SAUDE_ID.format(SQLPaciente._NOME_TABELA, plano_saude_id))
        paciente = cursor.fetchone()
        if not paciente:
            return None
        collumn_name = [desc[0] for desc in cursor.description]
        data = dict(zip(collumn_name, paciente))
        paciente = Paciente(**data)
        cursor.close()
        return paciente


    def get_by_nome(self, nome):
        cursor = self.data_base.cursor()
        cursor.execute(SQLPaciente._SCRIPT_SELECT_BUSCA.format(SQLPaciente._NOME_TABELA, nome))
        paciente = cursor.fetchone()
        if not paciente:
            return None
        collumn_name = [desc[0] for desc in cursor.description]
        data = dict(zip(collumn_name, paciente))
        paciente = Paciente(**data)
        cursor.close()
        return paciente


    def update(self, paciete_old, paciente_new):
        cursor = self.data_base.cursor()
        cursor.execute(SQLPaciente._SCRIPT_UPDATE, (paciente_new.nome, paciente_new.endereco, paciente_new.telefone,
                                                    paciente_new.email, paciente_new.data_nascimento,
                                                    paciente_new.data_primeira_consulta, paciente_new.plano_saude_id,
                                                    paciete_old.id))
        self.data_base.commit()
        cursor.close()


    def delete(self, id):
        cursor = self.data_base.cursor()
        cursor.execute(SQLPaciente._SCRIPT_DELETE.format(SQLPaciente._NOME_TABELA, id))
        self.data_base.commit()
        cursor.close()
