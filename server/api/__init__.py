from flask import Blueprint

api_resource = Blueprint('api_resource', __name__)
import api.urls

