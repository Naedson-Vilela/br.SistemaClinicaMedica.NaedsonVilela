from flask import Blueprint, make_response, request, jsonify
from app.modulos.Encaixe.dao import DaoEncaixe
from app.modulos.Consulta.dao import DaoConsulta
from app.modulos.Paciente.dao import DaoPaciente
from app.modulos.Consulta.model import Consulta
from app.util import validarFields

app_consulta = Blueprint('app_consulta', __name__)
app_name = 'consulta'
dao_consulta = DaoConsulta()
dao_encaixe = DaoEncaixe()
dao_paciente = DaoPaciente()


@app_consulta.route(f'/{app_name}/add/', methods=['POST'])
def add_consulta():
    validate, data = validarFields(request, Consulta)
    if not validate:
        return make_response(jsonify(data), 404)

    consulta = Consulta(**data)

    if not dao_paciente.get_by_id(consulta.paciente_id):
        return make_response({'erro': 'id paciente não existe'}, 404)

    encaixe = dao_encaixe.save_consulta(consulta)

    if encaixe:
        return make_response({'id': consulta.id,
                              'data_hora': consulta.data_hora,
                              'revisao': consulta.revisao,
                              'paciente_id': consulta.paciente_id}, 202)
    else:
        return make_response({'erro': 'Erro ao cadastrar consulta, encaixes da data completas, tente outra data'}, 404)


@app_consulta.route(f'/{app_name}/', methods=['GET'])
def get_all_consultas():
    consultas = dao_consulta.get_all()
    if consultas:
        data = [consulta.get_json() for consulta in consultas]
        return make_response(jsonify(data))
    return make_response({'erro': 'Não existem consultas cadastradas'})


@app_consulta.route(f'/{app_name}/consulta_<int:id>/', methods=['GET'])
def get_consulta_by_id(id: int):
    consulta = dao_consulta.get_by_id(id)
    if not consulta:
        return make_response({'erro': f'Consulta não encontrada: {id}'}, 404)

    return make_response(consulta.get_json(), 202)


@app_consulta.route(f'/{app_name}/paciente_<int:id>/', methods=['GET'])
def get_consulta_by_paciente_id(id: int):
    consultas = dao_consulta.get_by_paciente_id(id)
    if not consultas:
        return make_response({'erro': f'ID não encontrado ou não possui consultas cadastradas nesse id: {id}'}, 404)

    return make_response(jsonify([consulta.get_json() for consulta in consultas]))


@app_consulta.route(f'/{app_name}/consulta_<int:id>/', methods=['PUT'])
def update_paciente(id: int):
    validate, data = validarFields(request, Consulta)
    if not validate:
        return make_response(jsonify(data), 404)

    consulta_old = dao_consulta.get_by_id(id)
    if not consulta_old:
        return make_response({'erro': f'ID consulta não encontrado : {id}'}, 404)

    consulta_new = Consulta(**data)
    dao_consulta.update(consulta_old, consulta_new)
    consulta_new.id = consulta_old.id
    return make_response(consulta_new.get_json())


@app_consulta.route(f'/{app_name}/consulta_<int:id>/', methods=['DELETE'])
def delete_consulta(id: int):
    if not dao_consulta.get_by_id(id):
        return make_response({'erro': f'ID consulta não encontrado : {id}'}, 404)
    dao_consulta.delete(id)
    return make_response('Consulta removido com sucesso!', 200)
