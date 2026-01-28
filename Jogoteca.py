from flask import Flask, render_template

class Jogo:
    def __init__ (self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

app = Flask(__name__)
@app.route('/inicio')

def inicio():
    jogo1 = Jogo('Tetris', 'Puzzle', 'Atari')
    jogo2 = Jogo('God of War', 'Ação', 'PS2')
    jogo3 = Jogo('Skyrim', 'RPG', 'PC')
    lista_jogos = [jogo1, jogo2, jogo3]
    return render_template('Lista.html', titulo='Jogos', jogos= lista_jogos)

app.run(debug=True)