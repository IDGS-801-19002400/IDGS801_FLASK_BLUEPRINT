from flask import Blueprint, jsonify

maestros = Blueprint('maestros', __name__)

@maestros.route('/getmaestros', methods=['GET'])
def getmaes():
    return{'key': 'Maestros'}
