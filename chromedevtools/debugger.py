"""
Debugger

Debugger domain exposes JavaScript debugging capabilities. It allows setting and removing 
breakpoints, stepping through execution, exploring stack traces, etc.

https://developer.chrome.com/devtools/docs/protocol/1.1/debugger
"""

from __future__ import absolute_import, division, print_function, unicode_literals
from .mixins import CreateCommand, ReceiveData

class Debugger(CreateCommand, ReceiveData):

    def __init__(self, websocket_connection):
        self.ws = websocket_connection

    def can_set_script_source(self):
        """
        https://developer.chrome.com/devtools/docs/protocol/1.1/debugger#command-canSetScriptSource
        """
        raise NotImplementedError()

    def continue_to_location(self):
        """
        https://developer.chrome.com/devtools/docs/protocol/1.1/debugger#command-continueToLocation
        """
        raise NotImplementedError()

    def disable(self):
        """
        https://developer.chrome.com/devtools/docs/protocol/1.1/debugger#command-disable
        """
        raise NotImplementedError()

    def enable(self):
        """
        https://developer.chrome.com/devtools/docs/protocol/1.1/debugger#command-enable
        """
        raise NotImplementedError()

    def evaluate_on_call_frame(self):
        """
        https://developer.chrome.com/devtools/docs/protocol/1.1/debugger#command-evaluateOnCallFrame
        """
        raise NotImplementedError()

    def get_script_source(self):
        """
        https://developer.chrome.com/devtools/docs/protocol/1.1/debugger#command-getScriptSource
        """
        raise NotImplementedError()

    def pause(self):
        """
        https://developer.chrome.com/devtools/docs/protocol/1.1/debugger#command-pause
        """
        raise NotImplementedError()

    def remove_breakpoint(self):
        """
        https://developer.chrome.com/devtools/docs/protocol/1.1/debugger#command-removeBreakpoint
        """
        raise NotImplementedError()

    def search_in_context(self):
        """
        https://developer.chrome.com/devtools/docs/protocol/1.1/debugger#command-searchInContent
        """
        raise NotImplementedError()

    def set_breakpoint(self):
        """
        https://developer.chrome.com/devtools/docs/protocol/1.1/debugger#command-setBreakpoint
        """
        raise NotImplementedError()

    def set_breakpoint_by_url(self):
        """
        https://developer.chrome.com/devtools/docs/protocol/1.1/debugger#command-setBreakpointByUrl
        """
        raise NotImplementedError()

    def set_breakpoints_active(self):
        """
        https://developer.chrome.com/devtools/docs/protocol/1.1/debugger#command-setBreakpointsActive
        """
        raise NotImplementedError()

    def set_pause_on_exceptions(self):
        """
        https://developer.chrome.com/devtools/docs/protocol/1.1/debugger#command-setPauseOnExceptions
        """
        raise NotImplementedError()

    def set_script_source(self):
        """
        https://developer.chrome.com/devtools/docs/protocol/1.1/debugger#command-setScriptSource
        """
        raise NotImplementedError()

    def step_into(self):
        """
        https://developer.chrome.com/devtools/docs/protocol/1.1/debugger#command-stepInto
        """
        raise NotImplementedError()

    def step_out(self):
        """
        https://developer.chrome.com/devtools/docs/protocol/1.1/debugger#command-stepOut
        """
        raise NotImplementedError()

    def step_over(self):
        """
        https://developer.chrome.com/devtools/docs/protocol/1.1/debugger#command-stepOver
        """
        raise NotImplementedError()
