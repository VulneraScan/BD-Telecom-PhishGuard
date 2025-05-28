from flask import Flask, request, jsonify
from flask_cors import CORS
from twilio.rest import Client
from dotenv import load_dotenv
import os
from classifier import PhishClassifier

env_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(env_path)

app = Flask(__name__)
CORS(app)
twilio_client = Client(os.getenv('TWILIO_ACCOUNT_SID'), os.getenv('TWILIO_AUTH_TOKEN'))
TWILIO_NUM = os.getenv('TWILIO_PHONE_NUMBER')
classifier = PhishClassifier()
otp_store = {}

@app.route('/api/send_sms', methods=['POST'])
def send_sms():
    data = request.json
    to = data.get('to')
    otp = data.get('otp')
    if not to or not otp:
        return jsonify({'error': 'to and otp required'}), 400
    try:
        msg = twilio_client.messages.create(
            body=f"Your PhishGuard OTP is {otp}",
            from_=TWILIO_NUM,
            to=to
        )
        otp_store[to] = str(otp)
        return jsonify({'sid': msg.sid}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/predict', methods=['POST'])
def predict():
    data = request.json
    text = data.get('text', '')
    score = classifier.predict(text)
    return jsonify({'phishing_score': score}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
