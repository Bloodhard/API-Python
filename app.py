# API - Lugar para disponibilizar recursos e/ou funcionalidades. 
# 1. Objetivo - Criar um api qu disponibiliza a consulta, criação, edição e exclusão de livros.
# 2. URL base - localhost
# 3. Endpoints - 
    # - localhost/livros (GET)
    # - localhost/livros (POST)
    # - localhost/livros/id (GET)
    # - localhost/livro/id (PUT)
    # - localhost/livro/id (DELETE)
# 4. Quais recusrsos - Livros

from flask import Flask, jsonify, request
from db import livros

app = Flask(__name__)



#Consultar(todos)
@app.route('/livros',methods=['GET'])
def obter_livros():
    return jsonify(livros)

#Consultar(id, nome ou autor)

@app.route('/livros/<id>',methods=['GET'])
def obter_livro_id(id):
    livros_status = []
    for livro in livros:
        if livro.get('id') == id or livro.get('autor') == id or livro.get('titulo') == id or livro.get('estado') == id: 
                livros_status.append(livro)
    return jsonify(livros_status)

#Editar um livro por ID
@app.route('/livros/<id>',methods=['PUT'])
def editar_livro_id(id):
    livro_alterado = request.get_json()
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])

#Criar novo livro
@app.route('/livros', methods=['POST'])
def incluir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)

    return jsonify(livros)

#Excluir livro
@app.route('/livros/<id>', methods=['DELETE'])
def excluir_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
    
    
    return jsonify(livros)


app.run(port=5000,host='0.0.0.0',debug=True)