from flask import Flask
from app.database.connect import ConnectDataBase

from app.modulos.PlanoSaude.controller import app_plano_saude
from app.modulos.Paciente.controller import app_paciente
from app.modulos.Consulta.controller import app_consulta
from app.modulos.Encaixe.controller import app_encaixe

app = Flask(__name__)
app.config.from_object('config')
ConnectDataBase().init_table()

app.register_blueprint(app_plano_saude)
app.register_blueprint(app_paciente)
app.register_blueprint(app_consulta)
app.register_blueprint(app_encaixe)
