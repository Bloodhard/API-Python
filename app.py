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
        'autor': 'J.R.R Tolkien'
    },
    {
        'id': '2',
        'titulo': '1984',
        'autor': 'George Orwell'
    },
    {
        'id': '3',
        'titulo': 'Harry Potter e a Pedra Filosofal',
        'autor': 'J.K Howling'
    },
    {
        'id': '4',
        'titulo': 'A Arte da Guerra',
        'autor': 'Sun Tzu'
    },
    {
        'id': '5',
        'titulo': 'Dom Quixote',
        'autor': 'Miguel de Cervantes'
    },
        {
        'id': '6',
        'titulo': 'Apanhador no Campo de Centeio',
        'autor': 'J.D. Salinger'
    },
    {
        'id': '7',
        'titulo': 'Matar um Mockingbird',
        'autor': 'Harper Lee'
    },
    {
        'id': '8',
        'titulo': 'Cem Anos de Solidão',
        'autor': 'Gabriel García Márquez'
    },
    {
        'id': '9',
        'titulo': 'Crime e Castigo',
        'autor': 'Fyodor Dostoevsky'
    },
    {
        'id': '10',
        'titulo': 'Ulisses',
        'autor': 'James Joyce'
    },
    {
        'id': '11',
        'titulo': 'O Grande Gatsby',
        'autor': 'F. Scott Fitzgerald'
    },
    {
        'id': '12',
        'titulo': 'O Hobbit',
        'autor': 'J.R.R. Tolkien'
    },
    {
        'id': '13',
        'titulo': 'O Pequeno Príncipe',
        'autor': 'Antoine de Saint-Exupéry'
    },
    {
        'id': '14',
        'titulo': 'A Revolução dos Bichos',
        'autor': 'George Orwell'
    },
    {
        'id': '15',
        'titulo': 'Lolita',
        'autor': 'Vladimir Nabokov'
    },
        {
        'id': '16',
        'titulo': 'Os Miseráveis',
        'autor': 'Victor Hugo'
    },
    {
        'id': '17',
        'titulo': 'O Alquimista',
        'autor': 'Paulo Coelho'
    },
    {
        'id': '18',
        'titulo': 'A Odisséia',
        'autor': 'Homero'
    },
    {
        'id': '19',
        'titulo': 'A Metamorfose',
        'autor': 'Franz Kafka'
    },
    {
        'id': '20',
        'titulo': 'O Sol é para Todos',
        'autor': 'Harper Lee'
    },
    {
        'id': '21',
        'titulo': 'A Insustentável Leveza do Ser',
        'autor': 'Milan Kundera'
    },
    {
        'id': '22',
        'titulo': 'Dom Casmurro',
        'autor': 'Machado de Assis'
    },
    {
        'id': '23',
        'titulo': 'O Nome do Vento',
        'autor': 'Patrick Rothfuss'
    },
    {
        'id': '24',
        'titulo': 'O Silmarillion',
        'autor': 'J.R.R. Tolkien'
    },
    {
        'id': '25',
        'titulo': 'Cem Anos de Solidão',
        'autor': 'Gabriel García Márquez'
    },
        {
        'id': '26',
        'titulo': 'Introdução à Ciência da Computação',
        'autor': 'John Smith'
    },
    {
        'id': '27',
        'titulo': 'Algoritmos e Estruturas de Dados',
        'autor': 'Maria Silva'
    },
    {
        'id': '28',
        'titulo': 'Python para Iniciantes',
        'autor': 'Carlos Santos'
    },
    {
        'id': '29',
        'titulo': 'Machine Learning: Conceitos e Aplicações',
        'autor': 'Ana Pereira'
    },
    {
        'id': '30',
        'titulo': 'Redes de Computadores Avançadas',
        'autor': 'Luiz Oliveira'
    },
    {
        'id': '31',
        'titulo': 'Sistemas Operacionais Modernos',
        'autor': 'Paulo Rodrigues'
    },
    {
        'id': '32',
        'titulo': 'Banco de Dados Relacionais',
        'autor': 'Fernanda Costa'
    },
    {
        'id': '33',
        'titulo': 'Segurança da Informação',
        'autor': 'Ricardo Alves'
    },
    {
        'id': '34',
        'titulo': 'Desenvolvimento Web com Frameworks',
        'autor': 'Laura Mendes'
    },
    {
        'id': '35',
        'titulo': 'Inteligência Artificial Avançada',
        'autor': 'André Soares'
    },
        {
        'id': '36',
        'titulo': 'Arquitetura de Computadores Moderna',
        'autor': 'José Ramos'
    },
    {
        'id': '37',
        'titulo': 'Introdução à Inteligência Artificial',
        'autor': 'Mariana Santos'
    },
    {
        'id': '38',
        'titulo': 'Programação Paralela e Distribuída',
        'autor': 'Pedro Lima'
    },
    {
        'id': '39',
        'titulo': 'Sistemas de Informação Geográfica',
        'autor': 'Ana Almeida'
    },
    {
        'id': '40',
        'titulo': 'Aprendizado de Máquina com Python',
        'autor': 'Carlos Mendonça'
    },
    {
        'id': '41',
        'titulo': 'Segurança em Redes de Computadores',
        'autor': 'Fernando Gonçalves'
    },
    {
        'id': '42',
        'titulo': 'Desenvolvimento de Aplicativos Móveis',
        'autor': 'Luciana Ferreira'
    },
    {
        'id': '43',
        'titulo': 'Análise de Dados com Python',
        'autor': 'Ricardo Costa'
    },
    {
        'id': '44',
        'titulo': 'Redes Neurais Artificiais',
        'autor': 'Paula Rodrigues'
    },
    {
        'id': '45',
        'titulo': 'Segurança em Blockchain',
        'autor': 'Luiz Santos'
    },
        {
        'id': '46',
        'titulo': 'Redes Sem Fio Avançadas',
        'autor': 'Carolina Lima'
    },
    {
        'id': '47',
        'titulo': 'Introdução à Programação Java',
        'autor': 'Pedro Alves'
    },
    {
        'id': '48',
        'titulo': 'Machine Learning para Iniciantes',
        'autor': 'Mariana Fernandes'
    },
    {
        'id': '49',
        'titulo': 'Desenvolvimento de Software Ágil',
        'autor': 'Ricardo Pereira'
    },
    {
        'id': '50',
        'titulo': 'Sistemas Distribuídos',
        'autor': 'Fernando Silva'
    },
    {
        'id': '51',
        'titulo': 'Segurança em Sistemas Web',
        'autor': 'Laura Oliveira'
    },
    {
        'id': '52',
        'titulo': 'Big Data e Análise de Dados',
        'autor': 'Carlos Mendes'
    },
    {
        'id': '53',
        'titulo': 'Inteligência Artificial na Medicina',
        'autor': 'Mariana Santos'
    },
    {
        'id': '54',
        'titulo': 'Blockchain para Negócios',
        'autor': 'Fernando Gonçalves'
    },
    {
        'id': '55',
        'titulo': 'Programação Orientada a Objetos em C++',
        'autor': 'Luciana Ferreira'
    },
        {
        'id': '56',
        'titulo': 'Desenvolvimento de Aplicativos para Dispositivos Móveis',
        'autor': 'Ana Almeida'
    },
    {
        'id': '57',
        'titulo': 'Programação em Python Avançada',
        'autor': 'Carlos Mendonça'
    },
    {
        'id': '58',
        'titulo': 'Inteligência Artificial e Ética',
        'autor': 'Mariana Fernandes'
    },
    {
        'id': '59',
        'titulo': 'Segurança em Redes sem Fio',
        'autor': 'Ricardo Pereira'
    },
    {
        'id': '60',
        'titulo': 'Data Science: Fundamentos e Aplicações',
        'autor': 'Fernando Silva'
    },
    {
        'id': '61',
        'titulo': 'Desenvolvimento Web Responsivo',
        'autor': 'Laura Oliveira'
    },
    {
        'id': '62',
        'titulo': 'Programação Funcional em Haskell',
        'autor': 'Carlos Mendes'
    },
    {
        'id': '63',
        'titulo': 'Machine Learning na Indústria',
        'autor': 'Mariana Santos'
    },
    {
        'id': '64',
        'titulo': 'Blockchain e Contratos Inteligentes',
        'autor': 'Fernando Gonçalves'
    },
    {
        'id': '65',
        'titulo': 'Algoritmos Avançados de Otimização',
        'autor': 'Luciana Ferreira'
    },
        {
        'id': '66',
        'titulo': 'Inteligência Artificial na Indústria Automobilística',
        'autor': 'Ana Almeida'
    },
    {
        'id': '67',
        'titulo': 'Desenvolvimento de Jogos com Unity',
        'autor': 'Carlos Mendonça'
    },
    {
        'id': '68',
        'titulo': 'Aprendizado de Máquina para Visão Computacional',
        'autor': 'Mariana Fernandes'
    },
    {
        'id': '69',
        'titulo': 'Segurança em Internet das Coisas (IoT)',
        'autor': 'Ricardo Pereira'
    },
    {
        'id': '70',
        'titulo': 'Computação em Nuvem: Conceitos e Práticas',
        'autor': 'Fernando Silva'
    },
    {
        'id': '71',
        'titulo': 'Desenvolvimento de Aplicativos Android',
        'autor': 'Laura Oliveira'
    },
    {
        'id': '72',
        'titulo': 'Programação em C# para Aplicativos Desktop',
        'autor': 'Carlos Mendes'
    },
    {
        'id': '73',
        'titulo': 'Deep Learning: Teoria e Aplicações',
        'autor': 'Mariana Santos'
    },
    {
        'id': '74',
        'titulo': 'Blockchain e Criptomoedas',
        'autor': 'Fernando Gonçalves'
    },
    {
        'id': '75',
        'titulo': 'Algoritmos de Processamento de Linguagem Natural',
        'autor': 'Luciana Ferreira'
    },
]

#Consultar(todos)
@app.route('/livros',methods=['GET'])
def obter_livros():
    return jsonify(livros)

#Consultar(id, nome ou autor)
@app.route('/livros/<id>',methods=['GET'])
def obter_livro_id(id):
    for livro in livros:
        if livro.get('id') == id or livro.get('autor') == id or livro.get('titulo') == id:
            return jsonify(livro)
    return jsonify({'erroro': 'Livro não encontrado'}), 404

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


app.run(port=8080,host='localhost',debug=True)