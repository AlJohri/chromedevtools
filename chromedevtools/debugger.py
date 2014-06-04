"""
https://developer.chrome.com/devtools/docs/protocol/1.1/debugger

Commands
    Debugger.canSetScriptSource
    Debugger.continueToLocation
    Debugger.disable
    Debugger.enable
    Debugger.evaluateOnCallFrame
    Debugger.getScriptSource
    Debugger.pause
    Debugger.removeBreakpoint
    Debugger.searchInContent
    Debugger.setBreakpoint
    Debugger.setBreakpointByUrl
    Debugger.setBreakpointsActive
    Debugger.setPauseOnExceptions
    Debugger.setScriptSource
    Debugger.stepInto
    Debugger.stepOut
    Debugger.stepOver

"""

from __future__ import absolute_import, division, print_function, unicode_literals
from .mixins import CreateCommand, ReceiveData

class Debugger(CreateCommand, ReceiveData):

    def __init__(self, websocket_connection):
        self.ws = websocket_connection