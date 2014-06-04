"""
DOM

This domain exposes DOM read/write operations. Each DOM Node is represented with its 
mirror object that has an id. This id can be used to get additional information on the Node, 
resolve it into the JavaScript object wrapper, etc. It is important that client receives DOM events 
only for the nodes that are known to the client. Backend keeps track of the nodes that were 
sent to the client and never sends the same node twice. It is client's responsibility to collect 
information about the nodes that were sent to the client.

Note that iframe owner elements will return corresponding document elements as their child nodes.

https://developer.chrome.com/devtools/docs/protocol/1.1/dom
"""

from __future__ import absolute_import, division, print_function, unicode_literals
from .mixins import CreateCommand, ReceiveData

class DOM(CreateCommand, ReceiveData):

    def __init__(self, websocket_connection):
        self.ws = websocket_connection

    def get_attributes(self):
        """
        Returns attributes for the specified node.

        https://developer.chrome.com/devtools/docs/protocol/1.1/dom#command-getAttributes
        """
        raise NotImplementedError()

    def get_document(self):
        """
        Returns the root DOM node to the caller.

        https://developer.chrome.com/devtools/docs/protocol/1.1/dom#command-getDocument
        """
        command = self._create_command('DOM.getDocument')
        self.ws.send(command)
        data = self._recv()
        return data['result']

    def get_outer_html(self, node_id):
        """
        Returns node's HTML markup.

        https://developer.chrome.com/devtools/docs/protocol/1.1/dom#command-getOuterHTML

        Parameters
            nodeId ( NodeId )
                Id of the node to get markup for.

        """
        command = self._create_command('DOM.getOuterHTML', nodeId=node_id)
        self.ws.send(command)
        data = self._recv()
        return data['result']

    def hide_highlight(self):
        """
        https://developer.chrome.com/devtools/docs/protocol/1.1/dom#command-hideHighlight
        """
        raise NotImplementedError()

    def highlight_node(self):
        """
        Hides DOM node highlight.

        https://developer.chrome.com/devtools/docs/protocol/1.1/dom#command-highlightNode
        """
        raise NotImplementedError()

    def highlight_rect(self):
        """
        Highlights given rectangle. Coordinates are absolute with respect to the main frame viewport.

        https://developer.chrome.com/devtools/docs/protocol/1.1/dom#command-highlightRect
        """
        raise NotImplementedError()

    def move_to(self):
        """
        Moves node into the new container, places it before the given anchor.

        https://developer.chrome.com/devtools/docs/protocol/1.1/dom#command-moveTo
        """
        raise NotImplementedError()

    def query_selector(self):
        """
        Executes querySelector on a given node.

        https://developer.chrome.com/devtools/docs/protocol/1.1/dom#command-querySelector
        """
        raise NotImplementedError()

    def query_selector_all(self):
        """
        Executes querySelectorAll on a given node.

        https://developer.chrome.com/devtools/docs/protocol/1.1/dom#command-querySelectorAll
        """
        raise NotImplementedError()

    def remove_attribute(self):
        """
        Removes attribute with given name from an element with given id.

        https://developer.chrome.com/devtools/docs/protocol/1.1/dom#command-removeAttribute
        """
        raise NotImplementedError()

    def remove_node(self):
        """
        Removes node with given id.

        https://developer.chrome.com/devtools/docs/protocol/1.1/dom#command-removeNode
        """
        raise NotImplementedError()

    def request_child_nodes(self):
        """
        Requests that children of the node with given id are returned to the caller in form of 
        setChildNodes events where not only immediate children are retrieved, but all children 
        down to the specified depth.

        https://developer.chrome.com/devtools/docs/protocol/1.1/dom#command-requestChildNodes
        """
        raise NotImplementedError()

    def request_node(self):
        """
        Requests that the node is sent to the caller given the JavaScript node object reference. All 
        nodes that form the path from the node to the root are also sent to the client as a series of 
        setChildNodes notifications.        
        
        https://developer.chrome.com/devtools/docs/protocol/1.1/dom#command-requestNode
        """
        raise NotImplementedError()

    def resolve_node(self):
        """
        Resolves JavaScript node object for given node id.

        https://developer.chrome.com/devtools/docs/protocol/1.1/dom#command-resolveNode
        """
        raise NotImplementedError()

    def set_attribute_value(self):
        """
        Sets attribute for an element with given id.

        https://developer.chrome.com/devtools/docs/protocol/1.1/dom#command-setAttributeValue
        """
        raise NotImplementedError()

    def set_attributes_as_text(self):
        """
        Sets attributes on element with given id. This method is useful when user edits some existing 
        attribute value and types in several attribute name/value pairs.

        https://developer.chrome.com/devtools/docs/protocol/1.1/dom#command-setAttributesAsText
        """
        raise NotImplementedError

    def set_node_name(self):
        """
        Sets node name for a node with given id.

        https://developer.chrome.com/devtools/docs/protocol/1.1/dom#command-setNodeName
        """
        raise NotImplementedError

    def set_node_value(self):
        """
        Sets node value for a node with given id.

        https://developer.chrome.com/devtools/docs/protocol/1.1/dom#command-setNodeValue
        """
        raise NotImplementedError

    def set_outer_html(self):
        """
        Sets node HTML markup, returns new node id.

        https://developer.chrome.com/devtools/docs/protocol/1.1/dom#command-setOuterHTML
        """
        raise NotImplementedError
