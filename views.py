from json import load
import json
from utils import adicionar, deletar, editar, load_data, load_template, build_response, adicionar, editar
import urllib.parse
from database import *
from os import error, replace

req = '''POST / HTTP/1.1
Host: 0.0.0.0:8080
Connection: keep-alive
Content-Length: 25
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Origin: http://0.0.0.0:8080
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Referer: http://0.0.0.0:8080/
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9,pt;q=0.8

titulo=Sorvete+de+banana&detalhes=Coloque+uma+banana+no+congelador+e+espere.+Pronto%21+1%2B1%3D2.'''

def index(request):

    if request.startswith('POST'):
        request = request.replace('\r', '')  # Remove caracteres indesejados
        # Cabeçalho e corpo estão sempre separados por duas quebras de linha
        partes = request.split('\n\n')
        print(partes)
        #tira todo o resto e pga somente a parte do título que é o que interessa.
        corpo = partes[1]
        print("CORPO:" + str(corpo))
        # print(partes)
        params = {}
        # Preencha o dicionário params com as informações do corpo da requisição
        # O dicionário conterá dois valores, o título e a descrição.
        # Posteriormente pode ser interessante criar uma função que recebe a
        # requisição e devolve os parâmetros para desacoplar esta lógica.
        # Dica: use o método split da string e a função unquote_plus

        # titulo=Sorvete+de+banana 
        # detalhes=Coloque+uma+banana+no+congelador+e+espere.+Pronto%21+1%2B1%3D
        for chave_valor in corpo.split('&'):
            # essa chave valor será :[Sorvete+de+banana  , detalhes=Coloque+uma+banana+no+congelador+e+espere.+Pronto%21+1%2B1%3D2.]
            # então se começar com titulo, eu pego depois do = até o final e coloco no dicio, e aí todos esses + são substituidos por espaços.
            if chave_valor.startswith("titulo"):
                params["titulo"] = urllib.parse.unquote_plus(chave_valor[chave_valor.find("=")+1:], encoding="utf-8", errors="replace")
            if chave_valor.startswith("detalhes"):
                params["detalhes"] = urllib.parse.unquote_plus(chave_valor[chave_valor.find("=")+1:], encoding="utf-8", errors="replace")

        adicionar(params)

        return build_response(code=303, reason='See Other', headers='Location: /')

    # Cria uma lista de <li>'s para cada anotação
    # Se tiver curiosidade: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
    
    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(id= note.id, title= note.title, details=note.content)
        for note in load_data()
    ]
    notes = '\n'.join(notes_li)

    return build_response(load_template('index.html').format(notes=notes))


def  delete_views(request):

    if request.startswith('POST'):
        request = request.replace('\r', '')  # Remove caracteres indesejados
        # Cabeçalho e corpo estão sempre separados por duas quebras de linha
        partes = request.split('\n\n')
        print(partes)
        #tira todo o resto e pga somente a parte do título que é o que interessa.
        corpo = partes[1]
        print("CORPO:" + str(corpo))
        # print(partes)
        id = urllib.parse.unquote_plus(corpo[corpo.find("=")+1:], encoding="utf-8", errors="replace")

        id_int = int(id)

        deletar(id_int)

        return build_response(code=303, reason='See Other', headers='Location: /')

    # Cria uma lista de <li>'s para cada anotação
    # Se tiver curiosidade: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
    
    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(id= note.id, title= note.title, details=note.content)
        for note in load_data()
    ]
    notes = '\n'.join(notes_li)

    return build_response(load_template('index.html').format(notes=notes))


def edit_views(request):

    if request.startswith('POST'):
        request = request.replace('\r', '')  # Remove caracteres indesejados
        partes = request.split('\n\n')
        print(partes)
        corpo = partes[1]
        print("CORPO:" + str(corpo))
        params = {}

        id = urllib.parse.unquote_plus(corpo[corpo.find("=")+1:], encoding="utf-8", errors="replace")
        id_int = int(id.split('&')[0])
        print(id_int)

        for chave_valor in corpo.split('&'):
            # essa chave valor será :[Sorvete+de+banana  , detalhes=Coloque+uma+banana+no+congelador+e+espere.+Pronto%21+1%2B1%3D2.]
            # então se começar com titulo, eu pego depois do = até o final e coloco no dicio, e aí todos esses + são substituidos por espaços.
            if chave_valor.startswith("titulo"):
                params["titulo"] = urllib.parse.unquote_plus(chave_valor[chave_valor.find("=")+1:], encoding="utf-8", errors="replace")
            if chave_valor.startswith("detalhes"):
                params["detalhes"] = urllib.parse.unquote_plus(chave_valor[chave_valor.find("=")+1:], encoding="utf-8", errors="replace")


        editar(id_int, params)

        return build_response(code=303, reason='See Other', headers='Location: /')

    # Cria uma lista de <li>'s para cada anotação
    # Se tiver curiosidade: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
    
    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(id= note.id, title= note.title, details=note.content)
        for note in load_data()
    ]
    notes = '\n'.join(notes_li)

    return build_response(load_template('index.html').format(notes=notes))


