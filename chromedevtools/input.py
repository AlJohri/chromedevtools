"""
https://developer.chrome.com/devtools/docs/protocol/1.1/input

Commands
	Input.dispatchKeyEvent		https://developer.chrome.com/devtools/docs/protocol/1.1/input#command-dispatchKeyEvent
	Input.dispatchMouseEvent	https://developer.chrome.com/devtools/docs/protocol/1.1/input#command-dispatchMouseEvent

"""

from .mixins import CreateCommand, ReceiveData

class Input(CreateCommand, ReceiveData):

    def __init__(self, websocket_connection):
        self.ws = websocket_connection