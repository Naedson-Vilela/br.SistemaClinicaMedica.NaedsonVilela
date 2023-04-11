from flask import Blueprint, make_response, jsonify, request
from app.modulos.Encaixe.dao import DaoEncaixe
from app.modulos.Consulta.dao import DaoConsulta
from app.util import validarFields
from app.modulos.Encaixe.model import Encaixe
from app.modulos.Consulta.model import Consulta


app_encaixe = Blueprint('app_encaixe', __name__)
app_name = 'encaixe'
dao_encaixe = DaoEncaixe()
dao_consulta = DaoConsulta()

@app_encaixe.route(f'/{app_name}/', methods=['GET'])
def get_all_encaixes():
    encaixes = dao_encaixe.get_all()
    if encaixes:
        data = [encaixe.get_json() for encaixe in encaixes]
        return make_response(jsonify(data))
    return make_response({'erro': 'Não existem consultas cadastradas'})


@app_encaixe.route(f'/{app_name}/<int:id>/', methods=['GET'])
def get_encaixe_by_id(id: int):
    encaixe = dao_encaixe.get_by_id(id)
    if not encaixe:
        return make_response({'erro': f'Encaixe não encontrada: {id}'}, 404)

    return make_response(encaixe.get_json(), 202)

@app_encaixe.route(f'/{app_name}/<int:id>/consulta_<int:value>_id/', methods=['PUT'])
def remarcar_consulta(id: int, value: int):
    validate, data = validarFields(request, Consulta)
    if not validate:
        return make_response(jsonify(data), 404)
    if dao_consulta.get_by_id(dao_encaixe.get_consulta_id(id, value)):
        dao_consulta.delete(dao_encaixe.remarcar_consulta(id, value, data['data_hora']))
        return make_response(f'Consulta remarcada para a seguinte data: {data["data_hora"]}', 202)
    return make_response('Consulta não existe', 404)



@app_encaixe.route(f'/{app_name}/<int:id>/consulta_<int:value>_id/', methods=['DELETE'])
def delete_consulta_marcada(id: int, value: int):
    encaixe = dao_encaixe.get_by_id(id)
    if not encaixe:
        return make_response({'erro': f'ID encaixe não encontrado : {id}'}, 404)

    dao_consulta.delete(dao_encaixe.delete_consulta_marcada(id, value))

    return make_response(make_response('Consulta deletada'), 202)


@app_encaixe.route(f'/{app_name}/<int:id>/', methods=['DELETE'])
def delete_encaixe(id: int):
    if not dao_encaixe.get_by_id(id):
        return make_response({'erro': f'ID encaixe não encontrado : {id}'}, 404)
    dao_consulta.delete(id)
    return make_response('Consulta removido com sucesso!', 200)
