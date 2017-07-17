from flask import Flask


def create_app():
    app = Flask(__name__)

    @app.route('/'):
        return "OK"

    return app


if __name__ == '__main__':
    app = create_app()
    app.run('0.0.0.0', 5555)
