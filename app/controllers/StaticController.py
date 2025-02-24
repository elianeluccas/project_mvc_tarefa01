from flask import render_template

class StaticController:

    @staticmethod
    def home():
        return render_template('index.html')
