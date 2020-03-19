from flask import Flask
import os

app = Flask(__name__)


@app.route('/')
def index():
    return "Привет от приложения Flask. Ура, все работает!"


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
# внимание: заходить надо все равно по http://127.0.0.1:5000/

