from flask import Flask, render_template, request

app = Flask(__name__)

# Store GPS data
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
