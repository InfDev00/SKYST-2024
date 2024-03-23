from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index2.html')

@socketio.on('message')
def handle_message(data):
    print('Received message:', data)
    socketio.emit('message', data)

if __name__ == '__main__':
    socketio.run(app, port=4000, debug=True)