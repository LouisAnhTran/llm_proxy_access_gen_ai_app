from flask import request,jsonify

def send_inference_handler():
    return jsonify({"response":"Louis is computer science student from Singapore Univerversity of Technology and Design, and this is response generated from mock model"})