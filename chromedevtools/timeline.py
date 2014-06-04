"""
https://developer.chrome.com/devtools/docs/protocol/1.1/timeline

Commands
    Timeline.start  https://developer.chrome.com/devtools/docs/protocol/1.1/timeline#command-start
    Timeline.stop   https://developer.chrome.com/devtools/docs/protocol/1.1/timeline#command-stop
"""

from __future__ import absolute_import, division, print_function, unicode_literals
from .mixins import CreateCommand, ReceiveData

class Timeline(CreateCommand, ReceiveData):

    def __init__(self, websocket_connection):
        self.ws = websocket_connection