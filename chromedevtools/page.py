"""
https://developer.chrome.com/devtools/docs/protocol/1.1/page

Commands
    Page.clearGeolocationOverride
    Page.disable
    Page.enable
    Page.navigate
    Page.reload
    Page.setGeolocationOverride

"""

from __future__ import absolute_import, division, print_function, unicode_literals
from .mixins import CreateCommand, ReceiveData

class Page(CreateCommand, ReceiveData):

    def __init__(self, websocket_connection):
        self.ws = websocket_connection