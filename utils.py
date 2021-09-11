import json
from os import path
from database import *

def extract_route(requisicao):
    #exemplo: GET /img/logo-getit.png HTTP/1.1
    #separa primeiro a partir do GET / 
    if requisicao.startswith("GET /"):
        lista1 = requisicao.split("GET /")
        # Dessa separação o primeiro termo vai ser o GET /, e a partir do segundo vai ser o resto 
        #Mais uma vez peço para separar mas agora a partir do espaço
        #Com essa separação, tenho que o termo 0 vai ser o /img/logo-getit.png, o que quero!
    elif requisicao.startswith("POST /"):
        lista1 = requisicao.split("POST /")

    lista2 = lista1[1].split(" ")

    return lista2[0]


def read_file(filepath):
    print(filepath)
    string = str(filepath)
    extensao = string.split(".")
    tipo = extensao[1]
    print(tipo)
    # if tipo == "txt" or tipo == "html" or tipo == "css" or tipo =="js":
    #     with open(filepath, "rt") as text:
    #         lido = text.read()
    #         return lido
    # else:
    with open(filepath, "rb") as file:
        lido = file.read()
        return lido        


# Implemente a função load_data, que recebe o nome de um arquivo JSON e devolve o conteúdo do arquivo carregado
# como um objeto Python (A função deve assumir que este arquivo JSON está localizado dentro da pasta data). Por exemplo:
# se o conteúdo do arquivo data/dados.json for a string {"chave": "valor"}, sua função deve devolver o dicionário Python {"chave": "valor"} 
# para a entrada dados.json (note que o nome da pasta não é enviado como argumento). Dica: já existe uma função Python para isso 
# (e você viu em Design de Software).

def load_data():
    db = Database('banco')
    notes = db.get_all()
    return notes


# Implemente a função load_template que recebe o nome de um arquivo de template e devolve uma string com o conteúdo desse arquivo.
# O nome do arquivo não inclui o nome da pasta templates. Por exemplo: para a entrada index.html você deve carregar o conteúdo do arquivo templates/index.html.

def load_template(fileName):
    file = open('templates/' + fileName, encoding="UTF-8") 
    conteudo = file.read()
    file.close()
    return conteudo
    

# Ainda na função index(request) do arquivo views.py, adicione a nova anotação (que deverá estar armazenada em params['titulo'] e params['detalhes']) ao arquivo notes.json.
# Dica: crie uma função no arquivo utils.py que recebe a nova anotação e a adiciona à lista do arquivo notes.json.
def adicionar(dict):
    db = Database('banco')
    add_note = db.add(Note(title= dict['titulo'], content=dict['detalhes']))

def deletar(id):
    db = Database('banco')
    deletar = db.delete(id)

def editar(id, dict):
    db = Database('banco')
    update = db.update(Note(id= id, title = dict['titulo'], content=dict['detalhes']))

# Implemente a função build_response no arquivo utils.py. Ele deve receber os seguintes argumentos: build_response(body='', code=200, reason='OK', headers='') 
# (talvez você queira ler isso: https://docs.python.org/3/tutorial/controlflow.html#default-argument-values).
# Lembre-se de testar a sua função com python test_utils.py.

def build_response(body='', code=200, reason='OK', headers=''):
    if len(headers) != 0:
        convertido = ("HTTP/1.1 " + str(code)+ " " + reason + '\n' + headers + '\n\n' + body).encode()  
    else:
         convertido = ("HTTP/1.1 " + str(code)+ " " + reason + '\n\n' + body).encode()  
    return convertido
