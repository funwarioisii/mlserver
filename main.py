from flask import Flask, make_response


app = Flask(__name__, static_folder=None)

@app.route('/<string:file_name>', methods=["GET"])
def models(file_name):
    resp = make_response()
    resp.data = open(file_name, 'rb').read()
    resp.headers['Access-Control-Allow-Origin'] = ' *'

    return resp


if __name__ == "__main__":
    print(app.url_map)
    app.run(host='0.0.0.0', port=3000)

