from flask import Flask, jsonify
import os

app = Flask(__name__)


# Endpoint to read and serve JSON data from cmw.json
@app.route("/cmw", methods=["GET"])
def get_cmw_data():
	cmw_json_path = os.path.abspath(os.path.join(path, "outputs/cmw.json"))
	if os.path.exists(cmw_json_path):
		with open(cmw_json_path, "r") as file:
			data = file.read()
		return jsonify(data)
	else:
		return f"{cmw_json_path} not found", 404


# Endpoint to read and serve JSON data from latest_predictions.json
@app.route("/predictions", methods=["GET"])
def get_predictions_data():
	predictions_json_path = os.path.abspath(
		os.path.join(path, "outputs/latest_predictions.json")
	)
	if os.path.exists(predictions_json_path):
		with open(predictions_json_path, "r") as file:
			data = file.read()
		return jsonify(data)
	else:
		return f"{predictions_json_path} not found", 404


@app.route("/weights", methods=["GET"])
def get_weights_data():
	predictions_json_path = os.path.abspath(
		os.path.join(path, "weights/valiweights.json")
	)
	if os.path.exists(predictions_json_path):
		with open(predictions_json_path, "r") as file:
			data = file.read()
		return jsonify(data)
	else:
		return f"{predictions_json_path} not found", 404


if __name__ == "__main__":
	from waitress import serve

	path = "time-series-prediction-subnet/validation/"
	serve(app, host="0.0.0.0", port=80)
