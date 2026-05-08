import os
from flask import Flask, jsonify, request
from entities.trip import Trip

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return jsonify({'success': True, 'message': 'Hello World!'}), 200

@app.route('/trips', methods=['GET'])
def trips():
    trips = Trip.get_all()
    return trips

@app.route('/trip', methods=['POST'])
def save_trip():
    data = request.json
    trip = Trip(name=data['name'], city=data['city'], latitude=data['latitude'], longitude=data['longitude'])
    id = trip.save()
    success = id is not None
    return jsonify(success), 201

@app.route('/trip/<int:id>', methods=['PUT'])
def update_trip(id):
    data = request.json
    success = Trip.update(id, data['name'], data['city'], data['latitude'], data['longitude'])
    return jsonify(success), 200

@app.route('/trip/<int:id>', methods=['DELETE'])
def delete_trip(id):
    success = Trip.delete(id)
    return jsonify(success), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5001)))