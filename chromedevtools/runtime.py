"""
https://developer.chrome.com/devtools/docs/protocol/1.1/runtime

Commands
    Runtime.callFunctionOn      https://developer.chrome.com/devtools/docs/protocol/1.1/runtime#command-callFunctionOn
    Runtime.enable              https://developer.chrome.com/devtools/docs/protocol/1.1/runtime#command-enable
    Runtime.evaluate            https://developer.chrome.com/devtools/docs/protocol/1.1/runtime#command-evaluate
    Runtime.getProperties       https://developer.chrome.com/devtools/docs/protocol/1.1/runtime#command-getProperties
    Runtime.releaseObject       https://developer.chrome.com/devtools/docs/protocol/1.1/runtime#command-releaseObject
    Runtime.releaseObjectGroup  https://developer.chrome.com/devtools/docs/protocol/1.1/runtime#command-releaseObjectGroup

"""

from .mixins import CreateCommand, ReceiveData

class Runtime(CreateCommand, ReceiveData):

    def __init__(self, websocket_connection):
        self.ws = websocket_connection

    def evaluate(self, expression):
        command = self._create_command('Runtime.evaluate', expression=expression)
        self.ws.send(command)
        data = self._recv()
        return data['result']['result']

    def get_properties(self, object_id):
        command = self._create_command('Runtime.getProperties', objectId=object_id)
        self.ws.send(command)
        data = self._recv()
        return data['result']['result']
