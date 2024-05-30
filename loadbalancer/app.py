from flask import Flask
import os
from endpoints import lb_blueprint

app = Flask(__name__)

# Register the Blueprint
app.register_blueprint(lb_blueprint)

if __name__ == "_main_":
    app.run(host='0.0.0.0', port=5000)