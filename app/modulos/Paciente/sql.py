from datetime import datetime


class SQLPaciente:
    _NOME_TABELA = 'pacientes'
    _SCRIPT_CREATE_PACIENTE_TABLE = f'CREATE TABLE IF NOT EXISTS {_NOME_TABELA} (' \
                               f'id SERIAL PRIMARY KEY, ' \
                               f'nome VARCHAR(255) NOT NULL,' \
                               f'endereco VARCHAR(255) NOT NULL,' \
                               f'telefone VARCHAR(255) NOT NULL,' \
                               f'email VARCHAR(255) NOT NULL,' \
                               f'data_nascimento DATE NOT NULL,' \
                               f'plano_saude_id INT REFERENCES planos_saude(id),' \
                               f'data_primeira_consulta DATE' \
                               f')'

    _SCRIPT_INSERT = f'INSERT INTO {_NOME_TABELA}(nome, endereco, telefone, email, data_nascimento,' \
                     f'plano_saude_id)' \
                     f' VALUES (%s , %s, %s, %s, %s, %s) RETURNING id'

    _SCRIPT_SELECT_ALL = f"SELECT * FROM {_NOME_TABELA}"

    _SCRIPT_SELECT_BY_ID = 'SELECT * FROM {} WHERE ID={}'

    _SCRIPT_SELECT_BY_DATA_PRIMEIRA_CONSULTA = f'SELECT * FROM {_NOME_TABELA} WHERE data_primeira_consulta=%s'

    _SCRIPT_SELECT_BY_PLANO_SAUDE_ID = f'SELECT * FROM {_NOME_TABELA} WHERE plano_saude_id=%s'

    _SCRIPT_DELETE = 'DELETE FROM {} WHERE ID={}'

    _SCRIPT_UPDATE = f"UPDATE {_NOME_TABELA} SET " \
                     f"nome = %s," \
                     f"endereco = %s," \
                     f"telefone = %s," \
                     f"email = %s," \
                     f"data_nascimento = %s," \
                     f"data_primeira_consulta = %s," \
                     f"plano_saude_id = %s  " \
                     f"WHERE ID=%s"

    _SCRIPT_SELECT_BUSCA = "SELECT * FROM {} WHERE nome ILIKE '%{}%'"
