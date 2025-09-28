from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/eco-route', methods=['GET'])
def get_eco_route():
    try:
        origin = request.args.get('origin', '').strip()
        destination = request.args.get('destination', '').strip()
        
        if not origin or not destination:
            return jsonify({'error': 'Missing origin or destination'}), 400
        
        # MOCK DATA FOR DEMO - ALWAYS WORKS!
        # Simulates real Google Maps response
        mock_responses = [
            {
                'eta_minutes': 26,
                'distance_km': 12.5,
                'co2_savings': 'Saves 0.6kg CO2 compared to standard routes',
                'message': f'Eco-route found! 12.5 km in 26 mins from {origin} to {destination}',
                'status': 'success'
            },
            {
                'eta_minutes': 38,
                'distance_km': 18.5,
                'co2_savings': 'Saves 3.7kg CO2 compared to standard routes',
                'message': f'Eco-route found! 18.5 km in 38 mins from {origin} to {destination}',
                'status': 'success'
            },
            {
                'eta_minutes': 45,
                'distance_km': 22.3,
                'co2_savings': 'Saves 4.5kg CO2 compared to standard routes',
                'message': f'Eco-route found! 22.3 km in 45 mins from {origin} to {destination}',
                'status': 'success'
            }
        ]
        
        # Return different mock data based on origin (for realistic demo)
        if 'delhi' in origin.lower() or 'airport' in destination.lower():
            return jsonify(mock_responses[1])
        elif 'mumbai' in origin.lower():
            return jsonify(mock_responses[2])
        else:
            return jsonify(mock_responses[0])
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy', 'service': 'RideMate Eco-Route API'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
