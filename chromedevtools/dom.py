"""
https://developer.chrome.com/devtools/docs/protocol/1.1/dom

Commands
    DOM.getAttributes       https://developer.chrome.com/devtools/docs/protocol/1.1/dom#command-getAttributes
    DOM.getDocument         https://developer.chrome.com/devtools/docs/protocol/1.1/dom#command-getDocument
    DOM.getOuterHTML        https://developer.chrome.com/devtools/docs/protocol/1.1/dom#command-getOuterHTML
    DOM.hideHighlight       https://developer.chrome.com/devtools/docs/protocol/1.1/dom#command-hideHighlight
    DOM.highlightNode       https://developer.chrome.com/devtools/docs/protocol/1.1/dom#command-highlightNode
    DOM.highlightRect       https://developer.chrome.com/devtools/docs/protocol/1.1/dom#command-highlightRect
    DOM.moveTo              https://developer.chrome.com/devtools/docs/protocol/1.1/dom#command-moveTo
    DOM.querySelector       https://developer.chrome.com/devtools/docs/protocol/1.1/dom#command-querySelector
    DOM.querySelectorAll    https://developer.chrome.com/devtools/docs/protocol/1.1/dom#command-querySelectorAll
    DOM.removeAttribute     https://developer.chrome.com/devtools/docs/protocol/1.1/dom#command-removeAttribute
    DOM.removeNode          https://developer.chrome.com/devtools/docs/protocol/1.1/dom#command-removeNode
    DOM.requestChildNodes   https://developer.chrome.com/devtools/docs/protocol/1.1/dom#command-requestChildNodes
    DOM.requestNode         https://developer.chrome.com/devtools/docs/protocol/1.1/dom#command-requestNode
    DOM.resolveNode         https://developer.chrome.com/devtools/docs/protocol/1.1/dom#command-resolveNode
    DOM.setAttributeValue   https://developer.chrome.com/devtools/docs/protocol/1.1/dom#command-setAttributeValue
    DOM.setAttributesAsText https://developer.chrome.com/devtools/docs/protocol/1.1/dom#command-setAttributesAsText
    DOM.setNodeName         https://developer.chrome.com/devtools/docs/protocol/1.1/dom#command-setNodeName
    DOM.setNodeValue        https://developer.chrome.com/devtools/docs/protocol/1.1/dom#command-setNodeValue
    DOM.setOuterHTML        https://developer.chrome.com/devtools/docs/protocol/1.1/dom#command-setOuterHTML

"""

from .mixins import CreateCommand, ReceiveData

class DOM(CreateCommand, ReceiveData):

    def __init__(self, websocket_connection):
        self.ws = websocket_connection

    def get_document(self):
        command = self._create_command('DOM.getDocument')
        self.ws.send(command)
        data = self._recv()
        return data['result']

    def get_outer_html(self, node_id):
        command = self._create_command('DOM.getOuterHTML', nodeId=node_id)
        self.ws.send(command)
        data = self._recv()
        return data['result']
