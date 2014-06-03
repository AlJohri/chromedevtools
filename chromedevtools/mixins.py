import json

class CreateCommand:
    """
    Convert method name and params into the dict (json) to be sent via websockets
    """
    def _create_command(self, method, **params):
        command = {
            'id': 1,
            'method': method,
            'params': params
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
            # import pdb; pdb.set_trace()
            if data.get('method') == None: 
                break
        return data