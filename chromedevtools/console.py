"""
Console

Console domain defines methods and events for interaction with the JavaScript console. 
Console collects messages created by means of the JavaScript Console API. One needs to 
enable this domain using enable command in order to start receiving the console messages. 
Browser collects messages issued while console domain is not enabled as well and reports 
them using messageAdded notification upon enabling.

https://developer.chrome.com/devtools/docs/protocol/1.1/console
"""

from __future__ import absolute_import, division, print_function, unicode_literals
from .mixins import CreateCommand, ReceiveData

class Console(CreateCommand, ReceiveData):

    def __init__(self, websocket_connection):
        self.ws = websocket_connection

    def clear_messages(self):
        """
        https://developer.chrome.com/devtools/docs/protocol/1.1/console#command-clearMessages
        """
        raise NotImplementedError()

    def disable(self):
        """
        https://developer.chrome.com/devtools/docs/protocol/1.1/console#command-disable
        """
        raise NotImplementedError()

    def enable(self):
        """
        https://developer.chrome.com/devtools/docs/protocol/1.1/console#command-enable
        """
        raise NotImplementedError()