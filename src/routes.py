from flask import Blueprint, jsonify, request

routes = Blueprint('api', __name__)


@routes.route('/')
def default():
    return "hello from chat server", 200
