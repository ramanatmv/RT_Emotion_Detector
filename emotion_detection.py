# Import libraries
from flask import Flask, request, jsonify
import requests
import json
# Instantiate Flask functionality
app = Flask(__name__)
# Define the emotion detection function
def emotion_detector(text_to_analyse):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    Headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock", 'Content-Type': 'application/json'}
    Input_json = { "raw_document": { "text": text_to_analyse } }
    # Send a POST request to the Watson Emotion API and get the response
    response = requests.post(url, headers=headers, data=json.dumps(input_json))
    return response.json()
# Define the route for the emotion analysis endpoint
@app.route('/analyze', methods=['POST'])
def analyze_emotion():
    data = request.get_json()  # Get the JSON data from the request
    text_to_analyse = data.get('text', '')  # Extract the 'text_to_analyse' field from the JSON data
    if not text_to_analyse:  # Check if the text field is empty
        return jsonify({'error': 'No text provided'}), 400  # Return an error if no text is provided
    emotion_result = emotion_detector(text_to_analyse)  # Call the emotion detector function with the provided text
    return jsonify(emotion_result)  # Return the emotion detection results as a JSON response

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)