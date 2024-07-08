# web_interface.py
from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Mock data to simulate robot state
robot_state = {
    'x_position': 0,
    'y_position': 0,
    'arm_position': 0,
    'battery_level': 100,
    'current_task': 'Idle'
}

@app.route('/')
def index():
    return render_template('index.html', robot_state=robot_state)

@app.route('/move', methods=['POST'])
def move():
    data = request.json
    direction = data.get('direction')
    distance = data.get('distance')
    # Here you would add the code to move the robot
    # Example: move_robot(direction, distance)
    return jsonify({'status': 'success', 'direction': direction, 'distance': distance})

@app.route('/arm', methods=['POST'])
def arm():
    data = request.json
    position = data.get('position')
    # Here you would add the code to move the robot's arm
    # Example: move_arm(position)
    return jsonify({'status': 'success', 'position': position})

@app.route('/status', methods=['GET'])
def status():
    # Here you would update the robot_state with actual data from the robot
    return jsonify(robot_state)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
