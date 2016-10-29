import yaml
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/<country>")
def visa_reqs(country):
    doc = yaml.load(open('./data.yml'))
    return jsonify(dict(countries=doc[country]))

if __name__ == "__main__":
    app.run()

