from flask import render_template, request


class ProblemaController:
    @staticmethod
    def problema():
        return render_template('index.html')  # Página do formulário de entrada

    @staticmethod
    def resultado():
        # Coletando os valores do formulário
        var1 = request.form.get('var1')
        var2 = request.form.get('var2')

        if var1 and var2:
            # Realizando o cálculo
            resultado = int(var1) + int(var2)
            return render_template('resultado.html', var1=var1, var2=var2, resultado=resultado)
        else:
            return "Erro: Campos vazios", 400
