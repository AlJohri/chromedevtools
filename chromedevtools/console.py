"""
https://developer.chrome.com/devtools/docs/protocol/1.1/console

Commands
	Console.clearMessages	https://developer.chrome.com/devtools/docs/protocol/1.1/console#command-clearMessages
	Console.disable			https://developer.chrome.com/devtools/docs/protocol/1.1/console#command-disable
	Console.enable			https://developer.chrome.com/devtools/docs/protocol/1.1/console#command-enable

"""

from .mixins import CreateCommand, ReceiveData

class Console(CreateCommand, ReceiveData):

    def __init__(self, websocket_connection):
        self.ws = websocket_connection