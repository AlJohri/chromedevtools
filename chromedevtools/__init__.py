from __future__ import absolute_import, division, print_function, unicode_literals

import lxml.html
from websocket import create_connection

from .mixins import CreateCommand, ReceiveData
from .javascript import JS_FIND_CLICKABLE_ELEMENTS, JS_FIND_SCROLLABLE_ELEMENTS
from .console import Console
from .debugger import Debugger
from .dom import DOM
from .domdebugger import DOMDebugger
from .input import Input
from .network import Network
from .page import Page
from .runtime import Runtime
from .timeline import Timeline

class ChromeDevTools(CreateCommand, ReceiveData):

    def __init__(self, websocket_url):
        """
        Initialize websocket connection from string, ws.
        """
        self.ws = create_connection(websocket_url)

        self.console = Console(self.ws)
        self.debugger = Debugger(self.ws)
        self.dom = DOM(self.ws)
        self.domdebugger = DOMDebugger(self.ws)
        self.input = Input(self.ws)
        self.network = Network(self.ws)
        self.page = Page(self.ws)
        self.runtime = Runtime(self.ws)
        self.timeline = Timeline(self.ws)

    def close(self):
        self.ws.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    # High Level API

    def evaluate(self, expression):
        ret = self.runtime.evaluate(expression)
        remote_object = ret['objectId']
        object_properties = self.runtime.get_properties(remote_object)
        if ret['className'] == "Array":
            elements = list(filter(lambda prop: prop['name'].isdigit(), object_properties))
            return elements
        else:
            return object_properties

    def get_dom(self):
        doc = self.dom.get_document()
        root_id = doc['root']['nodeId']
        html = self.dom.get_outer_html(root_id)['outerHTML']
        dom = lxml.html.fromstring(html)
        return dom

    def get_clickable(self):
        return self.evaluate(JS_FIND_CLICKABLE_ELEMENTS)

    def get_scrollable(self):
        return self.evaluate(JS_FIND_SCROLLABLE_ELEMENTS)

    def click(self, x, y):
        return self.input.dispatch_mouse_event(x, y)

    def type(self, text):
        return self.input.dispatch_key_event(text)
