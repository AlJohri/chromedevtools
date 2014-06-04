"""
Network

Network domain allows tracking network activities of the page. It exposes information about 
http, file, data and other requests and responses, their headers, bodies, timing, etc.

https://developer.chrome.com/devtools/docs/protocol/1.1/network
"""

from __future__ import absolute_import, division, print_function, unicode_literals
from .mixins import CreateCommand, ReceiveData

class Network(CreateCommand, ReceiveData):

    def __init__(self, websocket_connection):
        self.ws = websocket_connection

    def can_clear_browser_cache(self):
        """
        https://developer.chrome.com/devtools/docs/protocol/1.1/network#command-canClearBrowserCache
        """
        raise NotImplementedError()

    def can_clear_browser_cookies(self):
        """
        https://developer.chrome.com/devtools/docs/protocol/1.1/network#command-canClearBrowserCookies
        """
        raise NotImplementedError()

    def clear_browser_cache(self):
        """
        https://developer.chrome.com/devtools/docs/protocol/1.1/network#command-clearBrowserCache
        """
        raise NotImplementedError()

    def clear_browser_cookies(self):
        """
        https://developer.chrome.com/devtools/docs/protocol/1.1/network#command-clearBrowserCookies
        """
        raise NotImplementedError()

    def disable(self):
        """
        https://developer.chrome.com/devtools/docs/protocol/1.1/network#command-disable
        """
        raise NotImplementedError()

    def enable(self):
        """
        https://developer.chrome.com/devtools/docs/protocol/1.1/network#command-enable
        """
        raise NotImplementedError()

    def get_response_body(self):
        """
        https://developer.chrome.com/devtools/docs/protocol/1.1/network#command-getResponseBody
        """
        raise NotImplementedError()

    def set_cache_disabled(self):
        """
        https://developer.chrome.com/devtools/docs/protocol/1.1/network#command-setCacheDisabled
        """
        raise NotImplementedError()

    def set_extra_http_headers(self):
        """
        https://developer.chrome.com/devtools/docs/protocol/1.1/network#command-setExtraHTTPHeaders
        """
        raise NotImplementedError()

    def set_user_agent_override(self):
        """
        https://developer.chrome.com/devtools/docs/protocol/1.1/network#command-setUserAgentOverride
        """
        raise NotImplementedError()
