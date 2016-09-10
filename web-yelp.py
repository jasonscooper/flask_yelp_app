from flask import Flask, render_template, request
import yelp_functions
import os
app = Flask(__name__)


@app.route("/")
def index():
	address = request.values.get('address')
	if address:
		businesses = yelp_functions.print_businesses("food", address)
	else:
		businesses = None
	return render_template('index.html', businesses=businesses)

@app.route('/about')
def about():
	return render_template('about.html')

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host="0.0.0.0", port=port)