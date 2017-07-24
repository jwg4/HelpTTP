from collections import defaultdict

from flask import Flask, request, jsonify, render_template

EXTRA_INFO = {
    header_tips: defaultdict(
        lambda: "",
        **{
            "Host": "By default, nginx reverse proxying will redefine this to the gateway host."
        }
    )
}


def create_app():
    app = Flask(__name__)

    def get_data(request):
        return {
            'headers': request.headers,
            'address': {
                'path': request.path,
                'full_path': request.full_path,
                'script_root': request.script_root,
                'url': request.url,
                'base_url': request.base_url,
                'url_root': request.url_root
            }
        }

    @app.route('/json')
    def get_json_data():
        data = get_data(request)
        return jsonify(data)

    @app.route('<path:dummy>')
    def get_html_data(dummy):
        print(dummy)
        if 'json' in dummy:
            return get_json_data()
        data = get_data(request)
        return render_template("index.html", data=data, extra=EXTRA_INFO)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run('0.0.0.0', 5555)
