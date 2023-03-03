from flask import Flask,redirect,url_for,render_template,request, jsonify

from Alumnos.routes import alumnos 
from Directivos.routes import directivos
from Maestros.routes import maestros

app=Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods=['GET'])
def home():
    return jsonify({'Datos':'Hello World'})

app.register_blueprint(alumnos)
app.register_blueprint(directivos)
app.register_blueprint(maestros)


if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run()