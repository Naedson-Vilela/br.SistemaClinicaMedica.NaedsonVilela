class SQLEncaixe:
    _NOME_TABELA = 'encaixes'
    _SCRIPT_CREATE_ENCAIXES_TABLE = f'CREATE TABLE IF NOT EXISTS {_NOME_TABELA} (' \
                                    f'id SERIAL PRIMARY KEY, ' \
                                    f'consulta_1_id INT REFERENCES consultas(id),' \
                                    f'consulta_2_id INT REFERENCES consultas(id),' \
                                    f'consulta_3_id INT REFERENCES consultas(id),' \
                                    f'data DATE UNIQUE' \
                                    f')'

    _SCRIPT_INSERT = f"INSERT INTO {_NOME_TABELA} (consulta_1_id, consulta_2_id, consulta_3_id, data)" \
                     " VALUES (NULL, NULL, NULL, '{}') RETURNING ID"

    _SCRIPT_SELECT_ALL = f"SELECT * FROM {_NOME_TABELA}"

    _SCRIPT_SELECT_BY_ID = 'SELECT * FROM {} WHERE ID={}'

    _SCRIPT_GET_CONSULTA_ID = 'SELECT consulta_{}_id FROM {} WHERE ID = {}'

    _SCRIPT_DELETE_CONSULTA_MARCADA = 'UPDATE {} SET consulta_{}_id = NULL WHERE ID = {}'

    _SCRIPTS_GET_BY_DATA = f"SELECT id, consulta_1_id, consulta_2_id, consulta_3_id, data FROM {_NOME_TABELA} " \
                           "WHERE data = '{}'"

    _SCRIPTS_UPDATE_CONSULTA = f"UPDATE {_NOME_TABELA} SET " \
                               "{} = {} " \
                               "WHERE data = '{}'"

    _SCRIPT_DELETE = 'DELETE FROM {} WHERE ID={}'

    _SCRIPT_UPDATE = "UPDATE {} SET " \
                     "data_hora = '{}', " \
                     "revisao = {}, " \
                     "paciente_id = {} " \
                     "WHERE ID={}"
