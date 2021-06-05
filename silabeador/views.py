from silabeador import app
from silabeador.tools import pilengua
from flask import jsonify

@app.route("/pilengua/<frase>")
def enlenguapi(frase):
    respuesta = pilengua(frase)
    d = {
        'originar': frase,
        'pilengua': respuesta
    }
    return jsonify(d)