from flask import render_template

class AutorController:
    @staticmethod
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
