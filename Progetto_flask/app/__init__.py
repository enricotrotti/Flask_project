from flask import Flask

app = Flask(__name__)
# Qui metto una chiave casuale che serve per
# la crittografia prevista dalle sessioni.
app.secret_key = 'abc123'

from . import routes
from . import models


# from flask import Flask, render_template
# def create_app():
#     app = Flask(__name__)

#     @app.route('/ind')
#     def index():
#         return render_template('index.html')
    

    
#     @app.route('/contributions')
#     def contributions():
#         return render_template('contributions.html')
    
#     @app.route('/talks')
#     def talks():
#         return render_template('talks.html')
    
    
#     return app
