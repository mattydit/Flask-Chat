from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = b'\xee\x84"JL9]IMl\xab\x91pd\x80`'
socketio = SocketIO(app)


@app.route('/')
def sessions():
    return render_template('session.html')

def messageReceived(methods=['GET', 'POST']):
    print('message was received!')


@socketio.on('message event')
def handleMessageEvent(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=messageReceived)


if __name__ == '__main__':
    socketio.run(app, debug=True)
