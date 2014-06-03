from __future__ import absolute_import, division, print_function, unicode_literals

from websocket import create_connection

from .mixins import CreateCommand, ReceiveData
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
