"""
Timeline

Timeline provides its clients with instrumentation records that are generated during the page 
runtime. Timeline instrumentation can be started and stopped using corresponding 
commands. While timeline is started, it is generating timeline event records.

https://developer.chrome.com/devtools/docs/protocol/1.1/timeline
"""

from __future__ import absolute_import, division, print_function, unicode_literals
from .mixins import CreateCommand, ReceiveData

class Timeline(CreateCommand, ReceiveData):

    def __init__(self, websocket_connection):
        self.ws = websocket_connection

    def start(self):
        """
        Starts capturing instrumentation events.

        https://developer.chrome.com/devtools/docs/protocol/1.1/timeline#command-start
        """
        raise NotImplementedError()

    def stop(self):
        """
        Stops capturing instrumentation events.
        
        https://developer.chrome.com/devtools/docs/protocol/1.1/timeline#command-stop
        """
        raise NotImplementedError()