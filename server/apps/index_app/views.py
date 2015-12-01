# coding: utf8
from flask import Blueprint, jsonify

index_app = Blueprint('index_app', __name__)


@index_app.route('/')
def index_view():
    response_data = {
        'message': 'hello'
    }
    return jsonify(response_data)
