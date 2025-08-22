from .db import get_db
from flask import render_template

from .models.ModeloMarco import ModeloMarco
from .models.ModeloVidrio import ModeloVidrio

def register_routes(app):

    @app.route('/')
    def index():
        db = get_db()
        marcos = ModeloMarco.listar_marcos(db)
        vidrios = ModeloVidrio.listar_vidrios(db)
        data = {
            'marcos': marcos,
            'vidrios': vidrios
        }
        return render_template('index.html', data=data)
