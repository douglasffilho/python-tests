from flask import Flask

from br.com.douglasffilho.controller.controller import Controller

app = Flask(__name__)

Controller(app)

if __name__ == '__main__':
    app.run()
