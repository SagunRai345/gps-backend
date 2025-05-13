from flask import Flask, request

app = Flask(__name__)

# To store GPS data
gps_data = []

@app.route('/')
def home():
    # Display the title and the current GPS data
    return """
    <html>
        <head><title>GPS DATA LOGGER</title></head>
        <body>
            <h1>GPS DATA LOGGER</h1>
            <h2>Current GPS Data:</h2>
            <ul>
                """ + ''.join([f"<li>Latitude: {data['lat']}, Longitude: {data['lng']}, Speed: {data['speed']} km/h</li>" for data in gps_data]) + """
            </ul>
        </body>
    </html>
    """

@app.route('/gps_data', methods=['GET'])
def gps_data_handler():
    lat = request.args.get('latitude')
    lng = request.args.get('longitude')
    speed = request.args.get('speed')

    if lat and lng and speed:
        # Append new GPS data
        gps_data.append({'lat': lat, 'lng': lng, 'speed': speed})
        return "Data stored", 200
    else:
        # Return a response indicating missing data
        return "Missing data", 400

if __name__ == '__main__':
    app.run(debug=True)
print("Received: ", lat, lng, speed)
