from flask import Flask, jsonify, render_template, request
from flask_socketio import SocketIO
import paho.mqtt.client as mqtt
from flask_cors import CORS
from datetime import datetime
import sqlite3
import time
import json

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

# MQTT Settings
MQTT_BROKER = 'localhost'
MQTT_TOPIC_SUBSCRIBE = 'sensor/data'
MQTT_TOPIC_PUBLISH = 'sensor/data2'

# Global variable to store the most recent message
latest_message = None

# Database setup
def init_db():
    conn = sqlite3.connect('sensor_data.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS sensor_readings
                 (timestamp TEXT, value1 REAL, value2 REAL, value3 REAL, value4 REAL)''')
    conn.commit()
    conn.close()

init_db()

# MQTT Callback Functions
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe(MQTT_TOPIC_SUBSCRIBE)

def on_message(client, userdata, msg):
    global latest_message
    message = msg.payload.decode()
    # string_list = message.split(',')
    # float_list = [float(item) for item in string_list]
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    formatted_data = {
        "time": timestamp,
        "value": message
    }
    
    print(f"Message received: {formatted_data}")
    latest_message = formatted_data
    socketio.emit('mqtt_message', {'data': formatted_data})
    
    # Save to database
    save_to_db(timestamp, message)

def save_to_db(timestamp, values):
    conn = sqlite3.connect('sensor_data.db')
    c = conn.cursor()
    c.execute("INSERT INTO sensor_readings VALUES (?, ?, ?, ?, ?)",
              (timestamp, values[0], values[1], values[2], values[3]))
    conn.commit()
    conn.close()

# Initialize MQTT Client
mqtt_client = mqtt.Client()
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message

try:
    mqtt_client.connect(MQTT_BROKER, 1883, 60)
    mqtt_client.loop_start()
except Exception as e:
    print(f"Failed to connect to MQTT broker: {e}")

@app.after_request
def add_cors_headers(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,POST')
    return response

@app.route('/')
def index():
    return render_template('lig.html')

@app.route('/messages', methods=['GET'])
def get_messages():
    global latest_message
    if latest_message is not None:
        return jsonify(latest_message)
    else:
        return jsonify({"message": "No data available yet"}), 204

@app.route('/receive_data', methods=['POST'])
def receive_data():
    if request.method == 'POST':
        data = request.json
        if data:
            print(f"Received data from app: {data}")
            
            formatted_data = data['value'] if 'value' in data else data
            
            # Publish the formatted data to MQTT topic
            mqtt_client.publish(MQTT_TOPIC_PUBLISH, json.dumps(formatted_data))
            
            socketio.emit('app_data', {'data': formatted_data})
            return jsonify({"status": "success", "message": "Data received and published"}), 200
        else:
            return jsonify({"status": "error", "message": "No data received"}), 400

@app.route('/get_all_data', methods=['GET'])
def get_all_data():
    conn = sqlite3.connect('sensor_data.db')
    c = conn.cursor()
    c.execute("SELECT * FROM sensor_readings ORDER BY timestamp DESC LIMIT 100")
    data = c.fetchall()
    conn.close()
    
    formatted_data = [{"time": row[0], "value": list(row[1:])} for row in data]
    return jsonify(formatted_data)

if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0", debug=True)