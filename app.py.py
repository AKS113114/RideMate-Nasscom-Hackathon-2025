from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

@app.route('/eco-route', methods=['GET'])
def get_eco_route():
    try:
        origin = request.args.get('origin', '').strip()
        destination = request.args.get('destination', '').strip()
        
        if not origin or not destination:
            return jsonify({'error': 'Missing origin or destination'}), 400
        
        # Call Google Maps API
        url = "https://maps.googleapis.com/maps/api/directions/json"
        params = {
            'origin': origin,
            'destination': destination,
            'alternatives': 'true',
            'key': GOOGLE_API_KEY
        }
        
        response = requests.get(url, params=params)
        data = response.json()
        
        if data['status'] != 'OK':
            return jsonify({'error': 'Google Maps API error'}), 500
        
        # Find shortest route
        eco_route = min(data['routes'], 
                       key=lambda x: x['legs'][0]['distance']['value'])
        
        leg = eco_route['legs'][0]
        distance_km = leg['distance']['value'] / 1000
        duration_mins = leg['duration']['value'] // 60
        co2_saved = distance_km * 0.2  # Simplified calculation
        
        return jsonify({
            'eta_minutes': duration_mins,
            'distance_km': round(distance_km, 1),
            'co2_savings': f"Saves {co2_saved:.1f}kg CO2",
            'message': f"Eco-route: {leg['distance']['text']} in {leg['duration']['text']}",
            'status': 'success'
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)