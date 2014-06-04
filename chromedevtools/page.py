"""
Page

Actions and events related to the inspected page belong to the page domain.

https://developer.chrome.com/devtools/docs/protocol/1.1/page
"""

from __future__ import absolute_import, division, print_function, unicode_literals
from .mixins import CreateCommand, ReceiveData

class Page(CreateCommand, ReceiveData):

    def __init__(self, websocket_connection):
        self.ws = websocket_connection

    def clear_geolocation_override(self):
        """
        Clears the overriden Geolocation Position and Error.

        https://developer.chrome.com/devtools/docs/protocol/1.1/page#command-clearGeolocationOverride
        """
        raise NotImplementedError()

    def disable(self):
        """
        Disables page domain notifications.

        https://developer.chrome.com/devtools/docs/protocol/1.1/page#command-disable
        """
        raise NotImplementedError()

    def enable(self):
        """
        Enables page domain notifications.

        https://developer.chrome.com/devtools/docs/protocol/1.1/page#command-enable
        """
        raise NotImplementedError()

    def navigate(self):
        """
        Navigates current page to the given URL.

        https://developer.chrome.com/devtools/docs/protocol/1.1/page#command-navigate
        """
        raise NotImplementedError()

    def relaod(self):
        """
        Reloads given page optionally ignoring the cache.

        https://developer.chrome.com/devtools/docs/protocol/1.1/page#command-reload
        """
        raise NotImplementedError()

    def set_geolocation_override(self):
        """
        Overrides the Geolocation Position or Error.

        https://developer.chrome.com/devtools/docs/protocol/1.1/page#command-setGeolocationOverride
        """
        raise NotImplementedError()
