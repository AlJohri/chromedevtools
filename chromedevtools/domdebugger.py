"""
https://developer.chrome.com/devtools/docs/protocol/1.1/domdebugger

Commands
    DOMDebugger.removeDOMBreakpoint             https://developer.chrome.com/devtools/docs/protocol/1.1/domdebugger#command-removeDOMBreakpoint
    DOMDebugger.removeEventListenerBreakpoint   https://developer.chrome.com/devtools/docs/protocol/1.1/domdebugger#command-removeEventListenerBreakpoint
    DOMDebugger.removeXHRBreakpoint             https://developer.chrome.com/devtools/docs/protocol/1.1/domdebugger#command-removeXHRBreakpoint
    DOMDebugger.setDOMBreakpoint                https://developer.chrome.com/devtools/docs/protocol/1.1/domdebugger#command-setDOMBreakpoint
    DOMDebugger.setEventListenerBreakpoint      https://developer.chrome.com/devtools/docs/protocol/1.1/domdebugger#command-setEventListenerBreakpoint
    DOMDebugger.setXHRBreakpoint                https://developer.chrome.com/devtools/docs/protocol/1.1/domdebugger#command-setXHRBreakpoint

"""

from .mixins import CreateCommand, ReceiveData

class DOMDebugger(CreateCommand, ReceiveData):

    def __init__(self, websocket_connection):
        self.ws = websocket_connection