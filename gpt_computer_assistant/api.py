# Create a python api and start_api function via flask

from flask import Flask, request, jsonify
import os
import sys
import threading
import time

app = Flask(__name__)

@app.route("/input", methods=["POST"])
def input():
    """
    This function receives input from the user and returns the response.
    """
    data = request.json
    text = data["text"]
    screen = data["screen"]
    print("Input:", text)
    from .gpt_computer_assistant import the_main_window, the_input_box
    if screen != "true":
        the_main_window.button_handler.input_text(text)
    else:
        the_main_window.button_handler.input_text_screenshot(text)
    
    time.sleep(1)
    while the_main_window.state != "idle":
        time.sleep(0.3)

    response = the_input_box.toPlainText()

    return jsonify({"response": response})

def start_api():
    """
    This function starts the API.
    """
    print("Starting API")
    threading.Thread(target=app.run, kwargs={"host": "0.0.0.0", "port": 7541}).start()
