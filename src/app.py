from flask import Flask, render_template, request,jsonify
import logging
from proxy import routes
from proxy.utils import helpers
from proxy.utils import CandidateQuestion

app = Flask(__name__)

# Configure logging
# declare logging format
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

candidate_question_instance=CandidateQuestion.CandidateQuestion()

@app.route("/get_sample_questions",methods=["GET"])
def get_sample_question():
    return routes.get_sample_questions_handler(candidate_question_instance)

@app.route("/get_suppored_models",methods=["GET"])
def get_supported_models():
    return routes.get_list_supported_models()

@app.route("/send_inference",methods=["POST"])
def send_inference():
    return routes.send_inference_handler(candidate_question_instance)

if __name__ == "__main__":
    app.run(debug=True,port=8000)
