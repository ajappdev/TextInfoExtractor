# app.py
import awsgi
from flask import Flask, request, jsonify
from word_info_extractor import analyze_text

app = Flask(__name__)

@app.route('/word-info', methods=['POST'])
def get_word_info():
    """
    This is the endpoint that we call in order to get the info of the
    input text
    """
    data = request.get_json()
    text = data.get('text', '')

    word_info = analyze_text(text)

    return jsonify(word_info)

def lambda_handler(event, context):
    """
    This is the function that we call upon invoking the lambda function
    """
    return awsgi.response(
        app, event, context, base64_content_types={"image/png"})

if __name__ == '__main__':
    app.run(debug=False)
