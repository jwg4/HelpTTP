from flask import Flask, request, jsonify, render_template


def create_app():
    app = Flask(__name__)

    def get_data(request):
        return {
            'headers': request.headers
        }

    @app.route('/<path:dummy>')
    def get_html_data(dummy):
        data = get_data(request)
        return render_template("index.html", data=data)

    @app.route('/json')
    def get_json_data():
        data = get_data(request)
        return jsonify(data)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run('0.0.0.0', 5555)
