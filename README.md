# br.SistemaClinicaMedica.NaedsonVilela
PYTHON | FLASK | POSTGRESQL. Sistema de simulação de controle de pacientes e consultas de uma clinica médica. Sistema desenvolvido durante a cadeira de Fundamentos de Bancos de Dados.

Paciente - String nome, endereco, telefone, email
           Date data de nascimento
           int plano_saude_id
           Date data_primeira_consulta


plano_saude - String nome
              int limite_consultas


consulta - Date data_hora
           boolean revisao
           int paciente_id

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
                                                ROTAS
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
                                               PACIENTE
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=


PACIENTE
{
    "data_nascimento": "1984-10-17",
    "data_primeira_consulta": null,
    "email": "hedonbolado@gmail.com",
    "endereco": "patos pb",
    "id": 1,
    "nome": "Heldon ",
    "plano_saude_id": "1",
    "telefone": "98999999999"
}


paciente -- /paciente/add/ -- POST
        Paciente - String nome, endereco, telefone, email
           Date data de nascimento 
           int plano_saude_id - null
           Date data_primeira_consulta - null

paciente -- /paciente/ -- GET
        Retorna todos os pacientes.

paciente -- /paciente/id -- GET
        Retorna paciente por ID

paciente -- /paciente/id -- PUT
        Atualiza paciente por ID

paciente -- /paciente/id -- DELETE
        Deleta paciente por ID

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
                                                CONSULTA
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

Consulta -- /cosnulta/add/ -- POST
        consulta - Date data_hora
           boolean revisao
           int paciente_id

Consulta -- /cosnulta/ -- GET
        Retorna todas as consultas

Consulta -- /cosnulta/id -- GET
        Retorna a consulta por id de paciente

Consulta -- /cosnulta/id -- PUT
        Atualiza a consulta por id da consulta
        consulta - Date data_hora
           boolean revisao
           int paciente_id

Consulta -- /cosnulta/id -- DELETE
        Deleta consulta por id de consulta

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
                                            PLANO DE SAUDE
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

Plano de Saude -- /plano_saude/add/ -- POST
        plano_saude - String nome
                      int limite_consultas

Plano de Saude -- /plano_saude/ -- GET
        Recupera todos os planos de saude

Plano de Saude -- /plano_saude/id/ -- GET
        Recupera plano de saude por ID

Plano de Saude -- /plano_saude/id/ -- PUT
        Atualiza plano de saude por ID

Plano de Saude -- /plano_saude/id/ -- DELETE
        Deleta plano de saude por ID

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
                                              ENCAIXE
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

Encaixe -- /encaixe/ -- GET
        Recupera todos os encaixes

Encaixe -- /encaixe/id/ -- GET
        Recupera o encaixe por id

Encaixe -- /encaixe/id/consulta_id/ -- PUT
        Atualiza todos o encaixe por id
        consulta - Date data_hora
           boolean revisao
           int paciente_id

Encaixe -- /encaixe/id/consulta_id/ -- DELETE
        Deleta a consulta do encaixe pelo id
        
Encaixe -- /encaixe/id/consulta_id/ -- DELETE
        Deleta o encaixe por id




