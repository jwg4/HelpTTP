from flask import Flask, request, jsonify


def create_app():
    app = Flask(__name__)

    def get_data(request):
        return {
            'headers': request.headers
        }

    @app.route('/'):
        return "OK"

    @app.route('/json'):
        data = get_data(request)
        return jsonify(data)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run('0.0.0.0', 5555)
