rom flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def hello():
	return jsonify(
{"about": "Hello there!"},
)

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
