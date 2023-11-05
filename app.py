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


app = Flask(__name__)

livros = [
    {
        'id': '1',
        'titulo': 'O Senhor dos Aneis - A Sociedade do Anel',
        'autor': 'J.R.R Tolkien',
        'estado': 'usado',
        'quantidade_de_livros': 3

    },
    {
        'id': '2',
        'titulo': '1984',
        'autor': 'George Orwell',
        'estado': 'usado',
        'quantidade_de_livros': 10
    },
    {
        'id': '3',
        'titulo': 'Harry Potter e a Pedra Filosofal',
        'autor': 'J.K Howling',
        'estado': 'novo',
        'quantidade_de_livros': 5
    },
    {
        'id': '4',
        'titulo': 'A Arte da Guerra',
        'autor': 'Sun Tzu',
        'estado': 'usado',
        'quantidade_de_livros': 10
    },
    {
        'id': '5',
        'titulo': 'Dom Quixote',
        'autor': 'Miguel de Cervantes',
        'estado': 'usado',
        'quantidade_de_livros': 3
    },
        {
        'id': '6',
        'titulo': 'Apanhador no Campo de Centeio',
        'autor': 'J.D. Salinger',
        'estado': 'novo',
        'quantidade_de_livros': 4
    },
    {
        'id': '7',
        'titulo': 'Matar um Mockingbird',
        'autor': 'Harper Lee',
        'estado': 'novo',
        'quantidade_de_livros': 10
    },
    {
        'id': '8',
        'titulo': 'Cem Anos de Solidão',
        'autor': 'Gabriel García Márquez',
        'estado': 'usado',
        'quantidade_de_livros': 14
    },
    {
        'id': '9',
        'titulo': 'Crime e Castigo',
        'autor': 'Fyodor Dostoevsky',
        'estado': 'novo',
        'quantidade_de_livros': 1
    },
    {
        'id': '10',
        'titulo': 'Ulisses',
        'autor': 'James Joyce',
        'estado': 'novo',
        'quantidade_de_livros': 0
    },
    {
        'id': '11',
        'titulo': 'O Grande Gatsby',
        'autor': 'F. Scott Fitzgerald',
        'estado': 'usado',
        'quantidade_de_livros': 0
    },
    {
        'id': '12',
        'titulo': 'O Hobbit',
        'autor': 'J.R.R. Tolkien',
        'estado': 'novo',
        'quantidade_de_livros': 3
    },
    {
        'id': '13',
        'titulo': 'O Pequeno Príncipe',
        'autor': 'Antoine de Saint-Exupéry',
        'estado': 'usado',
        'quantidade_de_livros': 4
    },
    {
        'id': '14',
        'titulo': 'A Revolução dos Bichos',
        'autor': 'George Orwell',
        'estado': 'novo',
        'quantidade_de_livros': 7
    },
    {
        'id': '15',
        'titulo': 'Lolita',
        'autor': 'Vladimir Nabokov',
        'estado': 'novo',
        'quantidade_de_livros': 1
    },
    {
        'id': '16',
        'titulo': 'Os Miseráveis',
        'autor': 'Victor Hugo',
        'estado': 'novo',
        'quantidade_de_livros': 10
    },
    {
        'id': '17',
        'titulo': 'O Alquimista',
        'autor': 'Paulo Coelho',
        'estado': 'usado',
        'quantidade_de_livros': 100
    },
    {
        'id': '18',
        'titulo': 'A Odisséia',
        'autor': 'Homero',
        'estado': 'novo',
        'quantidade_de_livros': 1
    },
    {
        'id': '19',
        'titulo': 'A Metamorfose',
        'autor': 'Franz Kafka',
        'estado': 'usado',
        'quantidade_de_livros': 23
    },
    {
        'id': '20',
        'titulo': 'O Sol é para Todos',
        'autor': 'Harper Lee',
        'estado': 'usado',
        'quantidade_de_livros': 3
    },
    {
        'id': '21',
        'titulo': 'A Insustentável Leveza do Ser',
        'autor': 'Milan Kundera',
        'estado': 'usado',
        'quantidade_de_livros': 5
    },
    {
        'id': '22',
        'titulo': 'Dom Casmurro',
        'autor': 'Machado de Assis',
        'estado': 'usado',
        'quantidade_de_livros': 5
    },
    {
        'id': '23',
        'titulo': 'O Nome do Vento',
        'autor': 'Patrick Rothfuss',
        'estado': 'usado',
        'quantidade_de_livros': 4
    },
    {
        'id': '24',
        'titulo': 'O Silmarillion',
        'autor': 'J.R.R. Tolkien',
        'estado': 'usado',
        'quantidade_de_livros': 5
    },
    {
        'id': '25',
        'titulo': 'Cem Anos de Solidão',
        'autor': 'Gabriel García Márquez',
        'estado': 'novo',
        'quantidade_de_livros': 5
    },
        {
        'id': '26',
        'titulo': 'Introdução à Ciência da Computação',
        'autor': 'John Smith',
        'estado': 'novo',
        'quantidade_de_livros': 3
    },
    {
        'id': '27',
        'titulo': 'Algoritmos e Estruturas de Dados',
        'autor': 'Maria Silva',
        'estado': 'novo',
        'quantidade_de_livros': 10
    },
    {
        'id': '28',
        'titulo': 'Python para Iniciantes',
        'autor': 'Carlos Santos',
        'estado': 'usado',
        'quantidade_de_livros': 5
    },
    {
        'id': '29',
        'titulo': 'Machine Learning: Conceitos e Aplicações',
        'autor': 'Ana Pereira',
        'estado': 'novo',
        'quantidade_de_livros': 4
    },
    {
        'id': '30',
        'titulo': 'Redes de Computadores Avançadas',
        'autor': 'Luiz Oliveira',
        'estado': 'usado',
        'quantidade_de_livros': 4
    },
    {
        'id': '31',
        'titulo': 'Sistemas Operacionais Modernos',
        'autor': 'Paulo Rodrigues',
        'estado': 'novo',
        'quantidade_de_livros': 4
    },
    {
        'id': '32',
        'titulo': 'Banco de Dados Relacionais',
        'autor': 'Fernanda Costa',
        'estado': 'usado',
        'quantidade_de_livros': 4
    },
    {
        'id': '33',
        'titulo': 'Segurança da Informação',
        'autor': 'Ricardo Alves',
        'estado': 'novo',
        'quantidade_de_livros': 6
    },
    {
        'id': '34',
        'titulo': 'Desenvolvimento Web com Frameworks',
        'autor': 'Laura Mendes',
        'estado': 'usado',
        'quantidade_de_livros': 2
    },
    {
        'id': '35',
        'titulo': 'Inteligência Artificial Avançada',
        'autor': 'André Soares',
        'estado': 'usado',
        'quantidade_de_livros': 10
    },
        {
        'id': '36',
        'titulo': 'Arquitetura de Computadores Moderna',
        'autor': 'José Ramos',
        'estado': 'novo',
        'quantidade_de_livros': 3
    },
    {
        'id': '37',
        'titulo': 'Introdução à Inteligência Artificial',
        'autor': 'Mariana Santos',
        'estado': 'novo',
        'quantidade_de_livros': 23
    },
    {
        'id': '38',
        'titulo': 'Programação Paralela e Distribuída',
        'autor': 'Pedro Lima',
        'estado': 'usado',
        'quantidade_de_livros': 15
    },
    {
        'id': '39',
        'titulo': 'Sistemas de Informação Geográfica',
        'autor': 'Ana Almeida',
        'estado': 'novo',
        'quantidade_de_livros': 10
    },
    {
        'id': '40',
        'titulo': 'Aprendizado de Máquina com Python',
        'autor': 'Carlos Mendonça',
        'estado': 'novo',
        'quantidade_de_livros': 15
    },
    {
        'id': '41',
        'titulo': 'Segurança em Redes de Computadores',
        'autor': 'Fernando Gonçalves',
        'estado': 'novo',
        'quantidade_de_livros': 12
    },
    {
        'id': '42',
        'titulo': 'Desenvolvimento de Aplicativos Móveis',
        'autor': 'Luciana Ferreira',
        'estado': 'novo',
        'quantidade_de_livros': 23
    },
    {
        'id': '43',
        'titulo': 'Análise de Dados com Python',
        'autor': 'Ricardo Costa',
        'estado': 'novo',
        'quantidade_de_livros': 10
    },
    {
        'id': '44',
        'titulo': 'Redes Neurais Artificiais',
        'autor': 'Paula Rodrigues',
        'estado': 'novo',
        'quantidade_de_livros': 4
    },
    {
        'id': '45',
        'titulo': 'Segurança em Blockchain',
        'autor': 'Luiz Santos',
        'estado': 'novo',
        'quantidade_de_livros': 4
    },
        {
        'id': '46',
        'titulo': 'Redes Sem Fio Avançadas',
        'autor': 'Carolina Lima',
        'estado': 'novo',
        'quantidade_de_livros': 4
    },
    {
        'id': '47',
        'titulo': 'Introdução à Programação Java',
        'autor': 'Pedro Alves',
        'estado': 'novo',
        'quantidade_de_livros': 4
    },
    {
        'id': '48',
        'titulo': 'Machine Learning para Iniciantes',
        'autor': 'Mariana Fernandes',
        'estado': 'novo',
        'quantidade_de_livros': 10
    },
    {
        'id': '49',
        'titulo': 'Desenvolvimento de Software Ágil',
        'autor': 'Ricardo Pereira',
        'estado': 'novo',
        'estado': 'usado',
        'quantidade_de_livros': 1
    },
    {
        'id': '50',
        'titulo': 'Sistemas Distribuídos',
        'autor': 'Fernando Silva',
        'estado': 'usado',
        'quantidade_de_livros': 1
    },
    {
        'id': '51',
        'titulo': 'Segurança em Sistemas Web',
        'autor': 'Laura Oliveira',
        'estado': 'usado',
        'quantidade_de_livros': 0
    },
    {
        'id': '52',
        'titulo': 'Big Data e Análise de Dados',
        'autor': 'Carlos Mendes',
        'estado': 'usado',
        'quantidade_de_livros': 15
    },
    {
        'id': '53',
        'titulo': 'Inteligência Artificial na Medicina',
        'autor': 'Mariana Santos',
        'estado': 'usado',
        'quantidade_de_livros': 0
    },
    {
        'id': '54',
        'titulo': 'Blockchain para Negócios',
        'autor': 'Fernando Gonçalves',
        'estado': 'usado',
        'quantidade_de_livros': 1
    },
    {
        'id': '55',
        'titulo': 'Programação Orientada a Objetos em C++',
        'autor': 'Luciana Ferreira',
        'estado': 'usado',
        'quantidade_de_livros': 15
    },
        {
        'id': '56',
        'titulo': 'Desenvolvimento de Aplicativos para Dispositivos Móveis',
        'autor': 'Ana Almeida',
        'estado': 'usado',
        'quantidade_de_livros': 1
    },
    {
        'id': '57',
        'titulo': 'Programação em Python Avançada',
        'autor': 'Carlos Mendonça',
        'estado': 'usado',
        'quantidade_de_livros': 0
    },
    {
        'id': '58',
        'titulo': 'Inteligência Artificial e Ética',
        'autor': 'Mariana Fernandes',
        'estado': 'usado',
        'quantidade_de_livros': 1
    },
    {
        'id': '59',
        'titulo': 'Segurança em Redes sem Fio',
        'autor': 'Ricardo Pereira',
        'estado': 'usado',
        'quantidade_de_livros': 3
    },
    {
        'id': '60',
        'titulo': 'Data Science: Fundamentos e Aplicações',
        'autor': 'Fernando Silva',
        'estado': 'usado',
        'quantidade_de_livros': 46
    },
    {
        'id': '61',
        'titulo': 'Desenvolvimento Web Responsivo',
        'autor': 'Laura Oliveira',
        'estado': 'usado',
        'quantidade_de_livros': 1
    },
    {
        'id': '62',
        'titulo': 'Programação Funcional em Haskell',
        'autor': 'Carlos Mendes',
        'estado': 'usado',
        'quantidade_de_livros': 1
    },
    {
        'id': '63',
        'titulo': 'Machine Learning na Indústria',
        'autor': 'Mariana Santos',
        'estado': 'usado',
        'quantidade_de_livros': 1
    },
]

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


app.run(port=5000,host='localhost',debug=True)