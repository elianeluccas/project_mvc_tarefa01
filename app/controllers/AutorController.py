from flask import render_template
from app.models.Autor import Autor

class AutorController:

    @staticmethod
    def autor():
        autor_info = Autor.obter_info()
        return render_template('autor.html', autor=autor_info)
