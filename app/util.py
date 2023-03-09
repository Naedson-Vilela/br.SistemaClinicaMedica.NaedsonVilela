from app.modulos.PlanoSaude.dao import DaoPlanoSaude
from app.modulos.Consulta.dao import DaoConsulta
from app.modulos.Paciente.dao import DaoPaciente
from app.modulos.Paciente.model import Paciente


def validarFields(request, objeto):
    data = request.form.to_dict()
    erros = []
    for key in objeto.FIELDS_TO_VALIDATE:
        if key not in data.keys():
            erros.append({
                'column': key,
                'message': 'Campo obrigatório'
            })
    if erros:
        return False, erros
    return data


def validar_plano_saude(id):
    plano_saude = DaoPlanoSaude().get_by_id(id)
    if not plano_saude:
        return False
    return True


def verificar_primeira_consulta(consulta):
    paciente = DaoPaciente().get_by_id(consulta.id)
    if paciente.plano_saude_id is None:
        paciente_new = Paciente(**paciente.get_json())
        paciente_new.data_primeira_consulta = str(consulta.data_hora)
        DaoPaciente().update(paciente, paciente_new)
        return True
    return False
