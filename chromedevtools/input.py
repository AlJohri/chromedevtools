"""
Input

https://developer.chrome.com/devtools/docs/protocol/1.1/input
"""

from __future__ import absolute_import, division, print_function, unicode_literals
from .mixins import CreateCommand, ReceiveData

class Input(CreateCommand, ReceiveData):

    def __init__(self, websocket_connection):
        self.ws = websocket_connection

    def dispatch_key_event(self, text=None, type="char", modifiers=None, timestamp=None, unmodified_text=None, key_identifier=None, windows_virtual_key_code=None, native_virtual_key_code=None, mac_char_code=None, auto_repeat=None, is_keypad=None, is_system_key=None):
        """
        Dispatches a key event to the page.

        https://developer.chrome.com/devtools/docs/protocol/1.1/input#command-dispatchKeyEvent

        Parameters
            type ( enumerated string [ "char" , "keyDown" , "keyUp" , "rawKeyDown" ] )
                Type of the key event.
            modifiers ( optional integer )
                Bit field representing pressed modifier keys. Alt=1, Ctrl=2, Meta/Command=4, Shift=8 (default: 0).
            timestamp ( optional number )
                Time at which the event occurred. Measured in UTC time in seconds since January 1, 1970 (default: current time).
            text ( optional string )
                Text as generated by processing a virtual key code with a keyboard layout. Not needed for for keyUp and rawKeyDown events (default: "")
            unmodified_text ( optional string )
                Text that would have been generated by the keyboard if no modifiers were pressed (except for shift). Useful for shortcut (accelerator) key handling (default: "").
            key_identifier ( optional string )
                Unique key identifier (e.g., 'U+0041') (default: "").
            windows_virtual_key_code ( optional integer )
                Windows virtual key code (default: 0).
            native_virtual_key_code ( optional integer )
                Native virtual key code (default: 0).
            mac_char_code ( optional integer )
                Mac character code (default: 0).
            auto_repeat ( optional boolean )
                Whether the event was generated from auto repeat (default: false).
            is_keypad ( optional boolean )
                Whether the event was generated from the keypad (default: false).
            is_system_key ( optional boolean )
                Whether the event was a system key event (default: false).        
        """
        command = self._create_command('Input.dispatchKeyEvent', 
            type=type, 
            modifiers=modifiers, 
            timestamp=timestamp, 
            text=text, 
            unmodifiedText=unmodified_text, 
            keyIdentifier=key_identifier, 
            windowsVirtualKeyCode=windows_virtual_key_code, 
            nativeVirtualKeyCode=native_virtual_key_code, 
            macCharCode=mac_char_code, 
            autoRepeat=auto_repeat, 
            isKeypad=is_keypad, 
            isSystemKey=is_system_key
        )
        self.ws.send(command)
        data = self._recv()
        return data

    def dispatch_mouse_event(self, x, y, type="mousePressed", modifiers=None, timestamp=None, button=None, click_count=None):
        """
        Dispatches a mouse event to the page.
        
        https://developer.chrome.com/devtools/docs/protocol/1.1/input#command-dispatchMouseEvent

        Parameters
            type ( enumerated string [ "mouseMoved" , "mousePressed" , "mouseReleased" ] )
                Type of the mouse event.
            x ( integer )
                X coordinate of the event relative to the main frame's viewport.
            y ( integer )
                Y coordinate of the event relative to the main frame's viewport. 0 refers to the top of the viewport and Y increases as it proceeds towards the bottom of the viewport.
            modifiers ( optional integer )
                Bit field representing pressed modifier keys. Alt=1, Ctrl=2, Meta/Command=4, Shift=8 (default: 0).
            timestamp ( optional number )
                Time at which the event occurred. Measured in UTC time in seconds since January 1, 1970 (default: current time).
            button ( optional enumerated string [ "left" , "middle" , "none" , "right" ] )
                Mouse button (default: "none").
            click_count ( optional integer )
                Number of times the mouse button was clicked (default: 0).        
        """
        command = self._create_command('Input.dispatchMouseEvent', 
            type=type, 
            x=x, 
            y=y, 
            modifiers=modifiers, 
            timestamp=timestamp, 
            button=button, 
            clickCount=click_count
        )
        self.ws.send(command)
        data = self._recv()
        return data