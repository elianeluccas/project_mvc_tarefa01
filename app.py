from flask import Flask, render_template, request
from app.controllers.ProblemaController import ProblemaController
from app.controllers.AutorController import AutorController
from app.controllers.StaticController import StaticController

app = Flask(__name__)
app.add_url_rule('/problema', 'problema', ProblemaController.problema)
app.add_url_rule('/resultado', 'resultado', ProblemaController.resultado)

# Rota para o formulário de entrada
@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Coletando os dados do formulário
        var1 = request.form.get('var1')
        var2 = request.form.get('var2')
        # Aqui você pode fazer cálculos com os valores recebidos
        resultado = int(var1) + int(var2)  # Exemplo de cálculo simples
        return render_template('resultado.html', resultado=resultado, var1=var1, var2=var2)
    return render_template('index.html')

# Rota para exibir o autor
@app.route('/autor')
def autor():
    autor_info = {
        'nome': 'Eliane Lucas',
        'formacao': [
            {'curso': 'Técnico em Informática', 'instituicao': 'IFSul de Minas', 'ano': '2024'},
            {'curso': 'Técnico em Informática para a Internet', 'instituicao': 'IFCE', 'ano': '2024'}
        ],
        'experiencias': [
            {'funcao': 'Estudante', 'empresa': 'IFCE', 'ano': '2024'},
            {'funcao': 'Estagiário de Desenvolvimento', 'empresa': 'DevSolutions', 'ano': '2024'}
        ]
    }
    return render_template('autor.html', autor=autor_info)

# Rota principal
@app.route('/')
def home():
    return "Bem-vindo à aplicação web com Flask!"

if __name__ == "__main__":
    app.run(debug=True)
