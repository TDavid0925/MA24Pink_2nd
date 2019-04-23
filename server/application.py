import os
from flask import Flask, render_template
from api import api_resource


"""
Make an application instance
"""
application = Flask(__name__, static_folder="../static/dist", template_folder="../static")

application.register_blueprint(api_resource)


"""
route configuration is here
"""
@application.route('/')
@application.route('/map')
@application.route('/journey')
def index():
    return render_template("index.html")
    


if __name__ == '__main__':
    application.debug = True
    application.run()