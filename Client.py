import logging
import _thread
from socketIO_client_nexus import SocketIO

logging.getLogger('socketIO-client').setLevel(logging.DEBUG)
logging.basicConfig()


def on_connect():
    print('connect')


def on_message(*args):
    print('message received!')


def on_disconnect():
    print('disconnect')


def on_reconnect():
    print('reconnect')


def on_server_message(*args):
    print('The server says: \"' + args[0] + "\"")


def on_lamp_update(*args):
    print('Lamp update received', args)


socketIO = SocketIO("http://18.188.195.129:3000", 3000)
socketIO.on('connect', on_connect)
socketIO.on('disconnect', on_disconnect)
socketIO.on('reconnect', on_reconnect)
# socketIO.on('message', on_message)
socketIO.on('server-message', on_server_message)
socketIO.on('lamp-update', on_lamp_update)

_thread.start_new_thread(socketIO.wait, ())

while True:
    user_in = input("Type \"touch\" to touch the lamp")
    if user_in == "touch":
        socketIO.emit('lamp-update', {'touch': True})
