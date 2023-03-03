from flask import Blueprint, jsonify

directivos = Blueprint('directivos', __name__)

@directivos.route('/getdirectivos', methods=['GET'])
def getdir():
    return{'key': 'Directivos'}
