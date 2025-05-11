from flask import Flask, request, jsonify

app = Flask(__name__)
gps_data = []

@app.route('/gps_data', methods=['GET'])
def gps_data_handler():
    lat = request.args.get('latitude')
    lng = request.args.get('longitude')
    speed = request.args.get('speed')

    if lat and lng and speed:
        gps_data.append({'lat': lat, 'lng': lng, 'speed': speed})
        return "Data stored", 200
    return "Missing data", 400

@app.route('/gps_data/view', methods=['GET'])
def view_all_data():
    return jsonify(gps_data)
