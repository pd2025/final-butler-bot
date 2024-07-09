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


available_sodas = ['Celsius','Moutain Dew', 'Dr. Pepper']
available_people =['Goli','Alex', 'Craig']

#probably have to change names
@app.route('/')
def index():
    return render_template('menu.html', robot_state=robot_state, sodas=available_sodas, people=available_people)

@app.route('/celisus_button')
def go_to_fridge():

    data = request.json
    soda = data.get('soda')
    person = data.get('person')
    # Here you would add the code to handle the autonomous delivery
    # Example: start_delivery_task(soda, person)
    robot_state['current_task'] = f'Delivering {soda} to {person}'
    return jsonify({'status': 'success', 'soda': soda, 'distance': person})


@app.route('/status', methods=['GET'])
def status():
    # Here you would update the robot_state with actual data from the robot
    return jsonify(robot_state)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
