import psycopg2
from app.modulos.PlanoSaude.sql import SQLPlanoSaude
from app.modulos.Paciente.sql import SQLPaciente
from app.modulos.Consulta.sql import SQLConsulta
from app.modulos.Encaixe.sql import SQLEncaixe


class ConnectDataBase:
    def __init__(self) -> None:
        self._connect = psycopg2.connect(
            host="localhost",
            database="SistemaClinica",
            user="postgres",
            password="postgres"
        )

    def get_instance(self):
        return self._connect

    def init_table(self):
        cursor = self._connect.cursor()
        cursor.execute(SQLPlanoSaude._SCRIPT_CREATE_PLANO_SAUDE_TABLE)
        cursor.execute(SQLPaciente._SCRIPT_CREATE_PACIENTE_TABLE)
        cursor.execute(SQLConsulta._SCRIPT_CREATE_CONSULTAS_TABLE)
        cursor.execute(SQLEncaixe._SCRIPT_CREATE_ENCAIXES_TABLE)
        self._connect.commit()
        cursor.close()

    def sql_new(self):
        return
