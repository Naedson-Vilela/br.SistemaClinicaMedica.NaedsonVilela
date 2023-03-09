class SQLConsulta:
    _NOME_TABELA = 'consultas'
    _SCRIPT_CREATE_CONSULTAS_TABLE = f'CREATE TABLE IF NOT EXISTS {_NOME_TABELA} (' \
                               f'id SERIAL PRIMARY KEY, ' \
                               f'data_hora DATE NOT NULL, ' \
                               f'revisao BOOLEAN NOT NULL, ' \
                               f'paciente_id INT REFERENCES pacientes(id))'

    _SCRIPT_INSERT = "INSERT INTO {} (data_hora, revisao, paciente_id)" \
                     " VALUES ('{}' , {}, {}) RETURNING id"

    _SCRIPT_SELECT_ALL = f"SELECT * FROM {_NOME_TABELA}"

    _SCRIPT_SELECT_BY_ID = 'SELECT * FROM {} WHERE ID={}'

    _SCRIPT_SELECT_BY_PACIENTE_ID = 'SELECT * FROM {} WHERE paciente_id={}'

    _SCRIPT_DELETE = 'DELETE FROM {} WHERE ID={}'

    _SCRIPT_UPDATE = "UPDATE {} SET " \
                     "data_hora = '{}', " \
                     "revisao = {}, " \
                     "paciente_id = {} " \
                     "WHERE ID={}"
