"""
Runtime

Runtime domain exposes JavaScript runtime by means of remote evaluation and mirror 
objects. Evaluation results are returned as mirror object that expose object type, string 
representation and unique identifier that can be used for further object reference. Original 
objects are maintained in memory unless they are either explicitly released or are released 
along with the other objects in their object group.

https://developer.chrome.com/devtools/docs/protocol/1.1/runtime
"""

from __future__ import absolute_import, division, print_function, unicode_literals
from .mixins import CreateCommand, ReceiveData

class Runtime(CreateCommand, ReceiveData):

    def __init__(self, websocket_connection):
        self.ws = websocket_connection

    def call_function_on(self):
        """
        Calls function with given declaration on the given object. Object group of the result is inherited 
        from the target object.

        https://developer.chrome.com/devtools/docs/protocol/1.1/runtime#command-callFunctionOn
        """
        raise NotImplementedError()

    def enable(self):
        """
        Enables reporting of execution contexts creation by means of executionContextCreated 
        event. When the reporting gets enabled the event will be sent immediately for each existing 
        execution context.

        https://developer.chrome.com/devtools/docs/protocol/1.1/runtime#command-enable
        """
        raise NotImplementedError()

    def evaluate(self, expression, return_by_value=False):
        """
        Evaluates expression on global object.

        https://developer.chrome.com/devtools/docs/protocol/1.1/runtime#command-evaluate
        """
        command = self._create_command('Runtime.evaluate', expression=expression, returnByValue=return_by_value)
        self.ws.send(command)
        data = self._recv()
        return data['result']['result']

    def get_properties(self, object_id):
        """
        Returns properties of a given object. Object group of the result is inherited from the target 
        object.

        https://developer.chrome.com/devtools/docs/protocol/1.1/runtime#command-getProperties
        """
        command = self._create_command('Runtime.getProperties', objectId=object_id)
        self.ws.send(command)
        data = self._recv()
        return data['result']['result']

    def release_object(self):
        """
        Releases remote object with given id.

        https://developer.chrome.com/devtools/docs/protocol/1.1/runtime#command-releaseObject
        """
        raise NotImplementedError()

    def release_object_group(self):
        """
        Releases all remote objects that belong to a given group.
        
        https://developer.chrome.com/devtools/docs/protocol/1.1/runtime#command-releaseObjectGroup
        """
        raise NotImplementedError()
