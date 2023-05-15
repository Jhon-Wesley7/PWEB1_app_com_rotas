from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Lista de clientes cadastrados (simulando um banco de dados)
clientes = []

@app.route('/')
def index():
    return render_template('index.html', clientes=clientes)

@app.route('/cadastrar')
def cadastrar():
    return render_template('cadastro.html')

@app.route('/adicionar', methods=['POST'])
def adicionar():
    nome = request.form['nome']
    email = request.form['email']
    telefone = request.form['telefone']

    cliente = {'nome': nome, 'email': email, 'telefone': telefone}
    clientes.append(cliente)

    return redirect('/')

@app.route('/editar/<int:id>', methods=['GET'])
def editar(id):
    cliente = None
    for c in clientes:
        if c['id'] == id:
            cliente = c
            break

    return render_template('edicao.html', cliente=cliente)

@app.route('/atualizar/<int:id>', methods=['POST'])
def atualizar(id):
    nome = request.form['nome']
    email = request.form['email']
    telefone = request.form['telefone']

    for c in clientes:
        if c['id'] == id:
            c['nome'] == nome
            c['email'] == email
            c['telefone'] == telefone
            break

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)