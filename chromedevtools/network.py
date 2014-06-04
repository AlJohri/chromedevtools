"""
https://developer.chrome.com/devtools/docs/protocol/1.1/network

Commands
    Network.canClearBrowserCache
    Network.canClearBrowserCookies
    Network.clearBrowserCache
    Network.clearBrowserCookies
    Network.disable
    Network.enable
    Network.getResponseBody
    Network.setCacheDisabled
    Network.setExtraHTTPHeaders
    Network.setUserAgentOverride

"""

from __future__ import absolute_import, division, print_function, unicode_literals
from .mixins import CreateCommand, ReceiveData

class Network(CreateCommand, ReceiveData):

    def __init__(self, websocket_connection):
        self.ws = websocket_connection