from flask import Flask, request, render_template

app = Flask(__name__)

# To store GPS data
gps_data = []

# Replace with your actual API key
API_KEY = 'your_api_key_here'

@app.route('/gps_data', methods=['GET'])
def gps_data_handler():
    api_key = request.args.get('api_key')
    if api_key != API_KEY:
        return "Unauthorized: Invalid API key", 403

    lat = request.args.get('latitude')
    lng = request.args.get('longitude')
    speed = request.args.get('speed')

    if lat and lng and speed:
        gps_data.append({'lat': lat, 'lng': lng, 'speed': speed})
        return "Data stored", 200
    else:
        return "Missing data", 400

@app.route('/')
def index():
    # Display GPS data on the home page
    if gps_data:
        last_data = gps_data[-1]  # Get the last data point
        return render_template('index.html', data=last_data)
    else:
        return render_template('index.html', data=None)

if __name__ == '__main__':
    app.run(debug=True)
