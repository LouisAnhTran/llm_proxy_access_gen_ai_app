from flask import Flask, render_template, request,jsonify

from src import routes

app = Flask(__name__)

@app.route("/send_inference",methods=["POST"])
def send_inference():
    return routes.send_inference_handler()

if __name__ == "__main__":
    app.run(debug=True,port=5050)
