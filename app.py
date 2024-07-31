from flask import Flask, request, jsonify, send_from_directory
import os
import google.generativeai as genai
from google.cloud import aiplatform

app = Flask(__name__)

API_KEY = "AIzaSyD0BD2TTBgqgsJZXnywHWgrZ1g1EIlie5g"
genai.configure(api_key=API_KEY)


@app.route('/generate', methods=['POST'])
def generate_text():
    prompt = request.json['prompt']
    try:
        response = genai.generate_text(prompt=prompt)
        generated_text = response.result if hasattr(response, 'result') else 'No result found in response'
        return jsonify({'response': generated_text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/')
def index():
    return send_from_directory('', 'templates/index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
