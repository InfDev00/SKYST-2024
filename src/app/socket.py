from flask_socketio import SocketIO

from app import socketio
from app.data import load_data


@socketio.on('request_json')
def send_json():
    data = load_data()
    socketio.emit('json_data', data)