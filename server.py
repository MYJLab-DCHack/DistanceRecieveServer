import sys 
sys.path.append('./')
from flask import Flask, request, jsonify
from lib.location_manager import LocationManager
from lib.calc_direction_and_distance import DirectionAndDistanceCalculator
from subprocess import Popen
import shellx

app = Flask(__name__)
location_manager = LocationManager()
ddc = DirectionAndDistanceCalculator()


@app.route('/', methods=["POST"])
def update_distance():
    user_id = request.json['user_id']
    distance = request.json["distance"]
    print(f"user_id: {user_id}, distance: {distance}")
    location_manager.update_distance(user_id, distance)
    return jsonify({
        "result": "ok"
    })

@app.route('/user/create', methods=["POST"])
def insert_user():
    user_id = request.json["user_id"]
    x = request.json["x"]
    y = request.json["y"]
    print(f"user_id: {user_id}, x: {x}, y; {y}")

@app.route('/comehere', methods=["POST"])
def comehere():
    user_id = request.json["user_id"]
    print(f"Device called by user: userId: {user_id}")
    return jsonify({
        "result": "ok"
    })

@app.route('/letter', methods=["POST"])
def send_letter():
    user_id = request.json["user_id"]
    to_user_id = request.json["to_user_id"]
    print(f"User {user_id} want to send letter to {to_user_id}")
    rotate = ddc
    return jsonify({
        "result": "ok"
    })

if __name__ == "__main__":
    loop_process = Popen("")
    app.run(debug=True, port=5000)

