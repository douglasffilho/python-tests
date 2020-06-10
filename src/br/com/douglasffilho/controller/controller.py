class Controller:

    def __init__(self, app):
        @app.route('/')
        def hello():
            return 'Hello World!'

        @app.route('/<name>')
        def hello_name(name):
            return f'Hello, {name}!'.format(name=name)
