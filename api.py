import flask
from flask import jsonify, request
import urllib.request, json

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/api/shoe-price/<id>', methods=['GET'])
def fetch_shoe_price(id):
    id = int(request.view_args['id'])
    url = f"https://bi8cxjuyll.execute-api.us-west-2.amazonaws.com/prices/shoes?id={id}"
    response = urllib.request.urlopen(url)
    data = response.read()
    return data

app.run(host="localhost", port=8081, debug=True)
