from flask import make_response, jsonify, request, Blueprint
from app.modulos.PlanoSaude.dao import DaoPlanoSaude
from app.modulos.PlanoSaude.model import PlanoSaude
from app.util import validarFields


app_plano_saude = Blueprint('plano_saude_blueprint', __name__)
app_name = 'plano_saude'
dao_plano_saude = DaoPlanoSaude()


@app_plano_saude.route(f'/{app_name}/add/', methods=['POST'])
def add_plano_saude():
    validate, data = validarFields(request, PlanoSaude)
    if not validate:
        print(data)
        return make_response(jsonify(data), 404)
    plano_saude = PlanoSaude(**data)
    dao_plano_saude.salvar(plano_saude)
    return make_response(plano_saude.get_json())


@app_plano_saude.route(f'/{app_name}/', methods=['GET'])
def get_planos_saude():
    planos_saude = dao_plano_saude.get_all()                        #Recuperando todos os planos de saude
    data = [plano_saude.get_json() for plano_saude in planos_saude]    #Adicionando os JSON de cada plano_saude dentro da lista
    return make_response(jsonify(data))                               #transformando a lista data em JSON e fazendo a response


@app_plano_saude.route(f'/{app_name}/<int:id>/', methods=['GET'])
def get_plano_saude_by_id(id: int):
    plano_saude = dao_plano_saude.get_by_id(id)
    if not plano_saude:
        return make_response({'ERRO': 'PLANO SAUDE NÃO ENCONTRADO!'}, 404)

    data = plano_saude.get_json()
    return make_response(data, 202)


@app_plano_saude.route(f'/{app_name}/<int:id>/', methods=['PUT'])
def update_plano_saude(id: int):
    validate, data = validarFields(request, PlanoSaude)
    if not validate:
        return make_response(jsonify(data), 404)

    plano_saude_old = dao_plano_saude.get_by_id(id)
    if not plano_saude_old:
        return make_response({'erro': f'ID não encontrado : {id}'}, 404)

    plano_saude_new = PlanoSaude(**data)
    dao_plano_saude.update_plano_saude(plano_saude_old, plano_saude_new)
    return make_response({'id': plano_saude_old.id,
                          'nome': plano_saude_new.nome,
                          'limite_consultas': plano_saude_new.limite_consultas})


@app_plano_saude.route(f'/{app_name}/<int:id>/', methods=['DELETE'])
def delete_plano_saude(id: int):
    if dao_plano_saude.get_by_id(id):
        dao_plano_saude.delete_plano_saude(id)
        return make_response({'Plano de saúde removido com sucesso!'}, 202)
    else:
        return make_response({'erro': f'ID inexistente: {id}'})
