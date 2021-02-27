from flask import Blueprint, jsonify, request
from logging import getLogger

routes = Blueprint('api', __name__)

logger = getLogger('app-log')

@routes.route('/')
def default():
    return "hello from chat server", 200

