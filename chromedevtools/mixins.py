from __future__ import absolute_import, division, print_function, unicode_literals

import json

class CreateCommand:
    """
    Convert method name and params into the dict (json) to be sent via websockets
    """
    def _create_command(self, method, **params):
        command = {
            'id': 1,
            'method': method,
            'params': dict((k, v) for k, v in params.iteritems() if v != None)
        }
        return json.dumps(command)

class ReceiveData:

    def _recv(self):
        """
        Get data from websocket connection ignoring all notifications.
        """
        while True:
            response = self.ws.recv()
            data = json.loads(response)
            if data.get('method') == None: 
                break
        return data