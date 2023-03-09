# from flask import make_response
from app.database.connect import ConnectDataBase
from app.modulos.PlanoSaude.sql import SQLPlanoSaude
from app.modulos.PlanoSaude.model import PlanoSaude


class DaoPlanoSaude:

    def __init__(self) -> None:
        self.data_base = ConnectDataBase().get_instance()

    def salvar(self, plano_saude):
        if plano_saude.id is None:
            cursor = self.data_base.cursor()
            cursor.execute(SQLPlanoSaude._SCRIPT_INSERT, (plano_saude.nome, plano_saude.limite_consultas))
            id = cursor.fetchone()[0]
            self.data_base.commit()
            cursor.close()
            plano_saude.id = id
            return plano_saude
        else:
            raise Exception("Erro ao cadastrar Plano de saúde!")

    def get_all(self):  # Método responsável por recuperar todos os planos de saude da tabela
        planos_saude = []
        cursor = self.data_base.cursor()
        cursor.execute(SQLPlanoSaude._SCRIPT_SELECT_ALL_)
        all_planos = cursor.fetchall()
        columns_name = [desc[0] for desc in
                        cursor.description]  # Esse trecho pega o nome de cada coluna e adiciona a uma lista
        for plano_saude_querry in all_planos:
            data = dict(zip(columns_name,
                            plano_saude_querry))  # Transforma em um dicionario o nome da tabela como key e a informação como value
            plano_saude = PlanoSaude(**data)
            planos_saude.append(plano_saude)
        cursor.close()
        if planos_saude:
            return planos_saude
        else:
            raise Exception('Não foi possivel recuperar os dados')

    def get_by_id(self, id):  # Métódo responsável por recuperar plano de saude por ID
        cursor = self.data_base.cursor()
        cursor.execute(SQLPlanoSaude._SCRIPT_SELECT_BY_ID.format(SQLPlanoSaude._NOME_TABELA, id))
        columns_name = [desc[0] for desc in cursor.description]
        plano_by_id = cursor.fetchone()
        if not plano_by_id:  # Caso nenhum plano seja encontrado com o ID informado retorna NONE
            return None
        data = dict(zip(columns_name, plano_by_id))
        plano_by_id = PlanoSaude(**data)
        cursor.close()
        return plano_by_id

    def update_plano_saude(self, plano_saude_old, plano_saude_new):
        cursor = self.data_base.cursor()
        cursor.execute(SQLPlanoSaude._SCRIPT_UPDATE, (plano_saude_new.nome,
                                                      plano_saude_new.limite_consultas,
                                                      plano_saude_old.id))
        self.data_base.commit()
        cursor.close()

    def delete_plano_saude(self, id):
        cursor = self.data_base.cursor()
        cursor.execute(SQLPlanoSaude._SCRIPT_DELETE, str(id))
        self.data_base.commit()
        cursor.close()

