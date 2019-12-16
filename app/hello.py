from flask import Flask
from app.services.nicks_code import ComplicatedThing
from flask import json
app = Flask(__name__)

@app.route("/jeff")
def hello():
	data = {'mydata': ComplicatedThing().perform_other_calc()}

	response = app.response_class(
		response=json.dumps(data),
		status=200,
		mimetype='application/json'
	)

	return response

@app.route("/nick")
def nick():
	return ComplicatedThing().perform_other_calc()

if __name__ == "__main__":
    app.run()