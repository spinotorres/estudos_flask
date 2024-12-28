from flask import Flask, render_template, request, redirect, session, flash

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

jogo1 = Jogo('WoW', 'MMORPG', 'PC')
jogo2 = Jogo('Diablo 3', 'RPG', 'PC, PS4, XBOX')
Jogo3 = Jogo('Skyrim', 'RPG', 'PC, PS4, XBOX')
Jogo4 = Jogo('God of War', 'Rack n Slash', 'PS2')
Jogo5 = Jogo('Dark Souls', 'RPG', 'PC, PS4, XBOX')

lista = [jogo1, jogo2, Jogo3, Jogo4, Jogo5]

app = Flask(__name__)
app.secret_key = 'spinola'

@app.route('/')
def index():
    return render_template('lista.html', 
                           titulo = 'Jogos', 
                           jogos = lista
                           )

@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect('/login?proxima=novo')
    return render_template('novo.html',
                           titulo='Novo Jogo'
                           )

@app.route('/criar', methods = ['POST', ])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']

    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect('/')

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima = proxima)

@app.route('/autenticar', methods = ['POST', ])
def autenticar():
    if 'mellon' == request.form['senha']:
        session['usuario_logado'] = request.form['usuario']
        flash(session['usuario_logado'] + ' logado com sucesso!')
        proxima_pagina = request.form['proxima']
        return redirect('/{}'.format(proxima_pagina))
    else:
        flash('Senha ou Usuário inválido!')
        return redirect('/login')

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Seção finalizada!')
    return redirect('/login')

app.run(debug = True)
