from flask import Flask
from users.controller import user_controller

app = Flask(__name__)

app.register_blueprint(user_controller.blueprint)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=8081)
