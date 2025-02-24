class Autor:

    @staticmethod
    def obter_info():
        return {
            'nome': 'João Silva',
            'formacao': [
                {'curso': 'Bacharelado em Ciência da Computação', 'instituicao': 'UFMG', 'ano': '2022'},
                {'curso': 'Mestrado em Engenharia de Software', 'instituicao': 'UFMG', 'ano': '2024'}
            ],
            'experiencias': [
                {'funcao': 'Desenvolvedor de Software', 'empresa': 'TechCorp', 'ano': '2023'},
                {'funcao': 'Estagiário de Desenvolvimento', 'empresa': 'DevSolutions', 'ano': '2022'}
            ]
        }
