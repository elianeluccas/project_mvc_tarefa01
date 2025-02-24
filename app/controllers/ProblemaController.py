from flask import render_template, request
from app.models.Problema import Problema

class ProblemaController:

    @staticmethod
    def index():
        return render_template('index.html')

    @staticmethod
    def problema():
        if request.method == 'POST':
            var1 = int(request.form.get('var1'))
            var2 = int(request.form.get('var2'))
            resultado = Problema.calcular(var1, var2)
            return render_template('problema.html', resultado=resultado, var1=var1, var2=var2)
        return render_template('problema.html', resultado=None)

    @staticmethod
    def resultado():
        return render_template("resultado.html")  # Certifique-se de que resultado.html existe!

