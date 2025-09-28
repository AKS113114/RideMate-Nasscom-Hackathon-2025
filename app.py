from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)  # <- This line is CRITICAL
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

@app.route('/eco-route', methods=['GET'])
def get_eco_route():
    # ... rest of your code ...

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
