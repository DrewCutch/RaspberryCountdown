import logging
import time
import _thread
from socketIO_client_nexus import SocketIO
from gpiozero import OutputDevice
from nixie_controller import NixieController
from nixie_display import  NixieDisplay

logging.getLogger('socketIO-client').setLevel(logging.DEBUG)
logging.basicConfig()

'''
First Nixie:
A : Pin 07 : GPIO4
B : Pin 11 : GPIO17
C : Pin 13 : GPIO27
D : Pin 15 : GPIO22

Second Nixie:
A : Pin 32 : GPIO12
B : Pin 36 : GPIO16
C : Pin 38 : GPIO20
D : Pin 40 : GPIO21
'''

nixieController1 = NixieController(0, 12, 21, 20, 16)
nixieController2 = NixieController(0, 4, 2, 22, 17)
nixieDisplay = NixieDisplay([nixieController1, nixieController2])


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


def on_lamp_update(data):
    print('Lamp update received', data)
    nixieDisplay.value = data["daysUntilVisit"]
    nixieDisplay.turn_on()
    time.sleep(10)
    nixieDisplay.turn_off()


socketIO = SocketIO("http://18.188.195.129:3000", 3000)
socketIO.on('connect', on_connect)
socketIO.on('disconnect', on_disconnect)
socketIO.on('reconnect', on_reconnect)
# socketIO.on('message', on_message)
socketIO.on('server-message', on_server_message)
socketIO.on('lamp-update', on_lamp_update)

_thread.start_new_thread(socketIO.wait, ())


nixieDisplay.turn_on()

for n in range(100):
    nixieDisplay.value = n
    time.sleep(1)

nixieDisplay.turn_off()

while True:
    user_in = input("Type \"touch\" to touch the lamp")
    if user_in == "touch":
        socketIO.emit('lamp-update', {'touch': True})
