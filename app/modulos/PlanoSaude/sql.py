class SQLPlanoSaude:
    _NOME_TABELA = 'planos_saude'
    _SCRIPT_CREATE_PLANO_SAUDE_TABLE = f'CREATE TABLE IF NOT EXISTS planos_saude (' \
                               f'id SERIAL PRIMARY KEY, ' \
                               f'nome VARCHAR(255) NOT NULL,' \
                               f'limite_consultas INTEGER NOT NULL' \
                               f')'
    _SCRIPT_INSERT = f'INSERT INTO {_NOME_TABELA}(nome, limite_consultas) VALUES (%s , %s) RETURNING id'
    _SCRIPT_SELECT_ALL_ = f"SELECT * FROM {_NOME_TABELA}"
    _SCRIPT_SELECT_BY_ID = 'SELECT * FROM {} WHERE ID={}'
    _SCRIPT_DELETE = f'DELETE FROM {_NOME_TABELA} WHERE ID=%s'
    _SCRIPT_UPDATE = f"UPDATE {_NOME_TABELA} SET nome = %s, limite_consultas = %s WHERE ID=%s"
