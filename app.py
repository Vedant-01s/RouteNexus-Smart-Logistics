# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
import time

app = Flask(__name__)
CORS(app) 

@app.route('/api/analyze', methods=['POST'])
def analyze_route():
    try:
        data = request.json
        shipment_id = data.get('id')
        weather = data.get('weather', '').lower()
        traffic = data.get('traffic', '').lower()

        time.sleep(1.5)

        if 'rain' in weather or 'flood' in weather or 'severe' in traffic:
            analysis = (
                f"Risk Level: HIGH\n\n"
                f"Conditions for {shipment_id} show severe weather ({weather}) and traffic ({traffic}) on the primary route, creating an 85% probability of major delay.\n\n"
                f"Recommendation: Immediately reroute via the Western Highway corridor to bypass the congested zones and save an estimated 4.5 hours of transit time."
            )
        else:
            analysis = (
                f"Risk Level: LOW\n\n"
                f"Current conditions for {shipment_id} indicate {weather} weather and {traffic} traffic. No significant disruptions detected.\n\n"
                f"Recommendation: Maintain current primary route. Continue standard monitoring."
            )

        return jsonify({
            "status": "success",
            "analysis": analysis
        })

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)