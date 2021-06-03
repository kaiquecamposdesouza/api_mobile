from flask import Flask, json
from BD import Seleciona

selec = Seleciona()

app = Flask(__name__)

class Usuario:
    def __init__(self, usuario, senha):
        self.login = usuario
        self.senha = senha

class Agenda_Banho_Tosa():
    def __init__(self, id, nome_pet, nome_proprietario, data, horario, funcionario, procedimento):
        self.id = id
        self.nome_pet = nome_pet
        self.proprietario = nome_proprietario
        self.data = data
        self.horario = horario
        self.funcionario = funcionario
        self.procedimento = procedimento

def cria_dic_agenda(lista):
    agenda_json = {}
    
    for dados in lista:
        agenda = Agenda_Banho_Tosa(dados[0], dados[1], dados[2], dados[3], dados[4], dados[5], dados[6])
        agenda_json[agenda.id] = {'id':agenda.id, 'nome_pet':agenda.nome_pet, 'proprietario':agenda.proprietario, 'data':str(agenda.data), 'horario':str(agenda.horario), 'funcionario':str(agenda.funcionario) , 'procedimento':agenda.procedimento}
        
    return agenda_json

def cria_dic_usuario(lista):
    usuario_json = {}
    
    for dados in lista:
        usuario = Usuario(dados[3], dados[4])
        usuario_json[usuario.login] = {'login':usuario.login, 'senha':usuario.senha}
        
    return usuario_json

def cria_json(dic, nome_arquivo):
    with open(str(nome_arquivo), 'w', encoding='utf8') as f:
        json.dump(dic, f, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ':'))

def ler_json(nome_arquivo):
    with open(str(nome_arquivo), 'r', encoding='utf8') as f:
        return json.load(f)


@app.route('/usuario', methods=['GET',])
def usuario():
    start = selec.start()
    seleciona_usuario = selec.selec_usuarios(start)
    dic_usuario = cria_dic_usuario(seleciona_usuario)
    usuario_json = cria_json(dic_usuario, 'usuario.json')
    ler_json_usuario = ler_json('usuario.json')

    return ler_json_usuario

@app.route('/agenda_banho_tosa', methods=['GET',])
def agenda():
    start = selec.start()
    seleciona_agendamento = selec.selec_agendamento_banho_tosa(start)
    dic_agenda = cria_dic_agenda(seleciona_agendamento)
    agenda_json = cria_json(dic_agenda, 'agenda.json')
    ler_json_agenda = ler_json('agenda.json')

    return ler_json_agenda

app.run()