"""
DOMDebugger

DOM debugging allows setting breakpoints on particular DOM operations and events. 
JavaScript execution will stop on these operations as if there was a regular breakpoint set.

https://developer.chrome.com/devtools/docs/protocol/1.1/domdebugger
"""

from __future__ import absolute_import, division, print_function, unicode_literals
from .mixins import CreateCommand, ReceiveData

class DOMDebugger(CreateCommand, ReceiveData):

    def __init__(self, websocket_connection):
        self.ws = websocket_connection

    def remove_dom_breakpoint(self):
        """
        https://developer.chrome.com/devtools/docs/protocol/1.1/domdebugger#command-removeDOMBreakpoint
        """
        raise NotImplementedError()

    def remove_event_listener_breakpoint(self):
        """
        https://developer.chrome.com/devtools/docs/protocol/1.1/domdebugger#command-removeEventListenerBreakpoint
        """
        raise NotImplementedError()

    def remove_xhr_breakpoint(self):
        """
        https://developer.chrome.com/devtools/docs/protocol/1.1/domdebugger#command-removeXHRBreakpoint
        """
        raise NotImplementedError()

    def set_dom_breakpoint(self):
        """
        https://developer.chrome.com/devtools/docs/protocol/1.1/domdebugger#command-setDOMBreakpoint
        """
        raise NotImplementedError()

    def set_event_listener_breakpoint(self):
        """
        https://developer.chrome.com/devtools/docs/protocol/1.1/domdebugger#command-setEventListenerBreakpoint
        """
        raise NotImplementedError()

    def set_xhr_breakpoint(self):
        """
        https://developer.chrome.com/devtools/docs/protocol/1.1/domdebugger#command-setXHRBreakpoint
        """
        raise NotImplementedError()
