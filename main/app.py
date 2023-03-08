from flask import Flask
from waitress import serve

app = Flask(__name__)

#escreva as rotas aqui

# aqui inicia o app e o servidor
if __name__ == "__main__":
    # comando para rodar via powershell: waitress-serve --host=127.0.0.1 --port=8080 tests.app:app
    serve(app, _quiet=True, host='127.0.0.1', port=8080, url_scheme='https')