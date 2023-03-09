from flask import make_response, request, Blueprint, jsonify
from app.modulos.Paciente.dao import DaoPaciente
from app.modulos.Paciente.model import Paciente
from app.util import validarFields, validar_plano_saude


app_paciente = Blueprint('paciente_blueprint', __name__)
app_name = 'paciente'
dao_paciente = DaoPaciente()


@app_paciente.route(f'/{app_name}/add/', methods=['POST'])
def add_paciente():
    data = validarFields(request, Paciente)
    if len(data) == 2:
        return make_response(jsonify(data), 404)

    if validar_plano_saude(data['plano_saude_id']):
        paciente = Paciente(**data)
        dao_paciente.salvar(paciente)
        return make_response(paciente.get_json(), 202)

    return make_response({'erro': 'Plano saude inválido'}, 404)


@app_paciente.route(f'/{app_name}/', methods=['GET'])
def get_all_pacientes():
    parametros = request.args
    busca = parametros.get('busca', None)
    paciente = dao_paciente.get_all(busca)
    data = [paciente.get_json() for paciente in paciente]
    return make_response(jsonify(data))


@app_paciente.route(f'/{app_name}/<int:id>/', methods=['GET'])
def get_paciente_by_id(id: int):
    paciente = dao_paciente.get_by_id(id)
    if not paciente:
        return make_response({'erro': 'ID não encontrado'}, 404)

    return make_response(paciente.get_json())


def get_paciente_by_plano_saude(id: int):
    pass

@app_paciente.route(f'/{app_name}/<int:id>/', methods=['PUT'])
def update_paciente(id: int):
    data = validarFields(request, Paciente)
    if len(data) == 2:
        return make_response(jsonify(data), 404)

    paciente_old = dao_paciente.get_by_id(id)
    if not paciente_old:
        return make_response({'erro': f'ID paciente não encontrado : {id}'}, 404)

    paciente_new = Paciente(**data)
    dao_paciente.update(paciente_old, paciente_new)
    paciente_new.id = paciente_old.id
    return make_response(paciente_new.get_json())



@app_paciente.route(f'/{app_name}/<int:id>/', methods=['DELETE'])
def delete_paciente(id: int):
    if not dao_paciente.get_by_id(id):
        return make_response({'erro': f'ID paciente não encontrado : {id}'}, 404)
    dao_paciente.delete(id)
    return make_response('Paciente removido com sucesso!', 200)
