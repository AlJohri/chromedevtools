
chromedevtools package
**********************


Submodules
==========


chromedevtools.console module
=============================

Console

Console domain defines methods and events for interaction with the
JavaScript console.  Console collects messages created by means of the
JavaScript Console API. One needs to  enable this domain using enable
command in order to start receiving the console messages.  Browser
collects messages issued while console domain is not enabled as well
and reports  them using messageAdded notification upon enabling.

https://developer.chrome.com/devtools/docs/protocol/1.1/console

class class chromedevtools.console.Console(websocket_connection)

   Bases: "chromedevtools.mixins.CreateCommand",
   "chromedevtools.mixins.ReceiveData"

   clear_messages()

      https://developer.chrome.com/devtools/docs/protocol/1.1/console
      #command-clearMessages

   disable()

      https://developer.chrome.com/devtools/docs/protocol/1.1/console
      #command-disable

   enable()

      https://developer.chrome.com/devtools/docs/protocol/1.1/console
      #command-enable


chromedevtools.debugger module
==============================

Debugger

Debugger domain exposes JavaScript debugging capabilities. It allows
setting and removing  breakpoints, stepping through execution,
exploring stack traces, etc.

https://developer.chrome.com/devtools/docs/protocol/1.1/debugger

class class chromedevtools.debugger.Debugger(websocket_connection)

   Bases: "chromedevtools.mixins.CreateCommand",
   "chromedevtools.mixins.ReceiveData"

   can_set_script_source()

      https://developer.chrome.com/devtools/docs/protocol/1.1/debugger
      #command-canSetScriptSource

   continue_to_location()

      https://developer.chrome.com/devtools/docs/protocol/1.1/debugger
      #command-continueToLocation

   disable()

      https://developer.chrome.com/devtools/docs/protocol/1.1/debugger
      #command-disable

   enable()

      https://developer.chrome.com/devtools/docs/protocol/1.1/debugger
      #command-enable

   evaluate_on_call_frame()

      https://developer.chrome.com/devtools/docs/protocol/1.1/debugger
      #command-evaluateOnCallFrame

   get_script_source()

      https://developer.chrome.com/devtools/docs/protocol/1.1/debugger
      #command-getScriptSource

   pause()

      https://developer.chrome.com/devtools/docs/protocol/1.1/debugger
      #command-pause

   remove_breakpoint()

      https://developer.chrome.com/devtools/docs/protocol/1.1/debugger
      #command-removeBreakpoint

   search_in_context()

      https://developer.chrome.com/devtools/docs/protocol/1.1/debugger
      #command-searchInContent

   set_breakpoint()

      https://developer.chrome.com/devtools/docs/protocol/1.1/debugger
      #command-setBreakpoint

   set_breakpoint_by_url()

      https://developer.chrome.com/devtools/docs/protocol/1.1/debugger
      #command-setBreakpointByUrl

   set_breakpoints_active()

      https://developer.chrome.com/devtools/docs/protocol/1.1/debugger
      #command-setBreakpointsActive

   set_pause_on_exceptions()

      https://developer.chrome.com/devtools/docs/protocol/1.1/debugger
      #command-setPauseOnExceptions

   set_script_source()

      https://developer.chrome.com/devtools/docs/protocol/1.1/debugger
      #command-setScriptSource

   step_into()

      https://developer.chrome.com/devtools/docs/protocol/1.1/debugger
      #command-stepInto

   step_out()

      https://developer.chrome.com/devtools/docs/protocol/1.1/debugger
      #command-stepOut

   step_over()

      https://developer.chrome.com/devtools/docs/protocol/1.1/debugger
      #command-stepOver


chromedevtools.dom module
=========================

DOM

This domain exposes DOM read/write operations. Each DOM Node is
represented with its  mirror object that has an id. This id can be
used to get additional information on the Node,  resolve it into the
JavaScript object wrapper, etc. It is important that client receives
DOM events  only for the nodes that are known to the client. Backend
keeps track of the nodes that were  sent to the client and never sends
the same node twice. It is client's responsibility to collect
information about the nodes that were sent to the client.

Note that iframe owner elements will return corresponding document
elements as their child nodes.

https://developer.chrome.com/devtools/docs/protocol/1.1/dom

class class chromedevtools.dom.DOM(websocket_connection)

   Bases: "chromedevtools.mixins.CreateCommand",
   "chromedevtools.mixins.ReceiveData"

   get_attributes()

      Returns attributes for the specified node.

      https://developer.chrome.com/devtools/docs/protocol/1.1/dom
      #command-getAttributes

   get_document()

      Returns the root DOM node to the caller.

      https://developer.chrome.com/devtools/docs/protocol/1.1/dom
      #command-getDocument

   get_outer_html(node_id)

      Returns node's HTML markup.

      https://developer.chrome.com/devtools/docs/protocol/1.1/dom
      #command-getOuterHTML

      Parameters
         nodeId ( NodeId )
            Id of the node to get markup for.

   hide_highlight()

      https://developer.chrome.com/devtools/docs/protocol/1.1/dom
      #command-hideHighlight

   highlight_node()

      Hides DOM node highlight.

      https://developer.chrome.com/devtools/docs/protocol/1.1/dom
      #command-highlightNode

   highlight_rect()

      Highlights given rectangle. Coordinates are absolute with
      respect to the main frame viewport.

      https://developer.chrome.com/devtools/docs/protocol/1.1/dom
      #command-highlightRect

   move_to()

      Moves node into the new container, places it before the given
      anchor.

      https://developer.chrome.com/devtools/docs/protocol/1.1/dom
      #command-moveTo

   query_selector()

      Executes querySelector on a given node.

      https://developer.chrome.com/devtools/docs/protocol/1.1/dom
      #command-querySelector

   query_selector_all()

      Executes querySelectorAll on a given node.

      https://developer.chrome.com/devtools/docs/protocol/1.1/dom
      #command-querySelectorAll

   remove_attribute()

      Removes attribute with given name from an element with given id.

      https://developer.chrome.com/devtools/docs/protocol/1.1/dom
      #command-removeAttribute

   remove_node()

      Removes node with given id.

      https://developer.chrome.com/devtools/docs/protocol/1.1/dom
      #command-removeNode

   request_child_nodes()

      Requests that children of the node with given id are returned to
      the caller in form of  setChildNodes events where not only
      immediate children are retrieved, but all children  down to the
      specified depth.

      https://developer.chrome.com/devtools/docs/protocol/1.1/dom
      #command-requestChildNodes

   request_node()

      Requests that the node is sent to the caller given the
      JavaScript node object reference. All  nodes that form the path
      from the node to the root are also sent to the client as a
      series of  setChildNodes notifications.

      https://developer.chrome.com/devtools/docs/protocol/1.1/dom
      #command-requestNode

   resolve_node()

      Resolves JavaScript node object for given node id.

      https://developer.chrome.com/devtools/docs/protocol/1.1/dom
      #command-resolveNode

   set_attribute_value()

      Sets attribute for an element with given id.

      https://developer.chrome.com/devtools/docs/protocol/1.1/dom
      #command-setAttributeValue

   set_attributes_as_text()

      Sets attributes on element with given id. This method is useful
      when user edits some existing  attribute value and types in
      several attribute name/value pairs.

      https://developer.chrome.com/devtools/docs/protocol/1.1/dom
      #command-setAttributesAsText

   set_node_name()

      Sets node name for a node with given id.

      https://developer.chrome.com/devtools/docs/protocol/1.1/dom
      #command-setNodeName

   set_node_value()

      Sets node value for a node with given id.

      https://developer.chrome.com/devtools/docs/protocol/1.1/dom
      #command-setNodeValue

   set_outer_html()

      Sets node HTML markup, returns new node id.

      https://developer.chrome.com/devtools/docs/protocol/1.1/dom
      #command-setOuterHTML


chromedevtools.domdebugger module
=================================

DOMDebugger

DOM debugging allows setting breakpoints on particular DOM operations
and events.  JavaScript execution will stop on these operations as if
there was a regular breakpoint set.

https://developer.chrome.com/devtools/docs/protocol/1.1/domdebugger

class class chromedevtools.domdebugger.DOMDebugger(websocket_connection)

   Bases: "chromedevtools.mixins.CreateCommand",
   "chromedevtools.mixins.ReceiveData"

   remove_dom_breakpoint()

      https://developer.chrome.com/devtools/docs/protocol/1.1/domdebu
      gger#command-removeDOMBreakpoint

   remove_event_listener_breakpoint()

      https://developer.chrome.com/devtools/docs/protocol/1.1/domdebu
      gger#command-removeEventListenerBreakpoint

   remove_xhr_breakpoint()

      https://developer.chrome.com/devtools/docs/protocol/1.1/domdebu
      gger#command-removeXHRBreakpoint

   set_dom_breakpoint()

      https://developer.chrome.com/devtools/docs/protocol/1.1/domdebu
      gger#command-setDOMBreakpoint

   set_event_listener_breakpoint()

      https://developer.chrome.com/devtools/docs/protocol/1.1/domdebu
      gger#command-setEventListenerBreakpoint

   set_xhr_breakpoint()

      https://developer.chrome.com/devtools/docs/protocol/1.1/domdebu
      gger#command-setXHRBreakpoint


chromedevtools.input module
===========================

Input

https://developer.chrome.com/devtools/docs/protocol/1.1/input

class class chromedevtools.input.Input(websocket_connection)

   Bases: "chromedevtools.mixins.CreateCommand",
   "chromedevtools.mixins.ReceiveData"

   dispatch_key_event(text=None, type=u'char', modifiers=None, timestamp=None, unmodified_text=None, key_identifier=None, windows_virtual_key_code=None, native_virtual_key_code=None, mac_char_code=None, auto_repeat=None, is_keypad=None, is_system_key=None)

      Dispatches a key event to the page.

      https://developer.chrome.com/devtools/docs/protocol/1.1/input
      #command-dispatchKeyEvent

      Parameters
         type ( enumerated string [ "char" , "keyDown" , "keyUp" ,
         "rawKeyDown" ] )
            Type of the key event.

         modifiers ( optional integer )
            Bit field representing pressed modifier keys. Alt=1,
            Ctrl=2, Meta/Command=4, Shift=8 (default: 0).

         timestamp ( optional number )
            Time at which the event occurred. Measured in UTC time in
            seconds since January 1, 1970 (default: current time).

         text ( optional string )
            Text as generated by processing a virtual key code with a
            keyboard layout. Not needed for for keyUp and rawKeyDown
            events (default: "")

         unmodified_text ( optional string )
            Text that would have been generated by the keyboard if no
            modifiers were pressed (except for shift). Useful for
            shortcut (accelerator) key handling (default: "").

         key_identifier ( optional string )
            Unique key identifier (e.g., 'U+0041') (default: "").

         windows_virtual_key_code ( optional integer )
            Windows virtual key code (default: 0).

         native_virtual_key_code ( optional integer )
            Native virtual key code (default: 0).

         mac_char_code ( optional integer )
            Mac character code (default: 0).

         auto_repeat ( optional boolean )
            Whether the event was generated from auto repeat (default:
            false).

         is_keypad ( optional boolean )
            Whether the event was generated from the keypad (default:
            false).

         is_system_key ( optional boolean )
            Whether the event was a system key event (default: false).

   dispatch_mouse_event(x, y, type=u'mousePressed', modifiers=None, timestamp=None, button=None, click_count=None)

      Dispatches a mouse event to the page.

      https://developer.chrome.com/devtools/docs/protocol/1.1/input
      #command-dispatchMouseEvent

      Parameters
         type ( enumerated string [ "mouseMoved" , "mousePressed" ,
         "mouseReleased" ] )
            Type of the mouse event.

         x ( integer )
            X coordinate of the event relative to the main frame's
            viewport.

         y ( integer )
            Y coordinate of the event relative to the main frame's
            viewport. 0 refers to the top of the viewport and Y
            increases as it proceeds towards the bottom of the
            viewport.

         modifiers ( optional integer )
            Bit field representing pressed modifier keys. Alt=1,
            Ctrl=2, Meta/Command=4, Shift=8 (default: 0).

         timestamp ( optional number )
            Time at which the event occurred. Measured in UTC time in
            seconds since January 1, 1970 (default: current time).

         button ( optional enumerated string [ "left" , "middle" ,
         "none" , "right" ] )
            Mouse button (default: "none").

         click_count ( optional integer )
            Number of times the mouse button was clicked (default: 0).


chromedevtools.javascript module
================================


chromedevtools.mixins module
============================

class class chromedevtools.mixins.CreateCommand

   Convert method name and params into the dict (json) to be sent via
   websockets

class class chromedevtools.mixins.ReceiveData


chromedevtools.network module
=============================

Network

Network domain allows tracking network activities of the page. It
exposes information about  http, file, data and other requests and
responses, their headers, bodies, timing, etc.

https://developer.chrome.com/devtools/docs/protocol/1.1/network

class class chromedevtools.network.Network(websocket_connection)

   Bases: "chromedevtools.mixins.CreateCommand",
   "chromedevtools.mixins.ReceiveData"

   can_clear_browser_cache()

      https://developer.chrome.com/devtools/docs/protocol/1.1/network
      #command-canClearBrowserCache

   can_clear_browser_cookies()

      https://developer.chrome.com/devtools/docs/protocol/1.1/network
      #command-canClearBrowserCookies

   clear_browser_cache()

      https://developer.chrome.com/devtools/docs/protocol/1.1/network
      #command-clearBrowserCache

   clear_browser_cookies()

      https://developer.chrome.com/devtools/docs/protocol/1.1/network
      #command-clearBrowserCookies

   disable()

      https://developer.chrome.com/devtools/docs/protocol/1.1/network
      #command-disable

   enable()

      https://developer.chrome.com/devtools/docs/protocol/1.1/network
      #command-enable

   get_response_body()

      https://developer.chrome.com/devtools/docs/protocol/1.1/network
      #command-getResponseBody

   set_cache_disabled()

      https://developer.chrome.com/devtools/docs/protocol/1.1/network
      #command-setCacheDisabled

   set_extra_http_headers()

      https://developer.chrome.com/devtools/docs/protocol/1.1/network
      #command-setExtraHTTPHeaders

   set_user_agent_override()

      https://developer.chrome.com/devtools/docs/protocol/1.1/network
      #command-setUserAgentOverride


chromedevtools.page module
==========================

Page

Actions and events related to the inspected page belong to the page
domain.

https://developer.chrome.com/devtools/docs/protocol/1.1/page

class class chromedevtools.page.Page(websocket_connection)

   Bases: "chromedevtools.mixins.CreateCommand",
   "chromedevtools.mixins.ReceiveData"

   clear_geolocation_override()

      Clears the overriden Geolocation Position and Error.

      https://developer.chrome.com/devtools/docs/protocol/1.1/page
      #command-clearGeolocationOverride

   disable()

      Disables page domain notifications.

      https://developer.chrome.com/devtools/docs/protocol/1.1/page
      #command-disable

   enable()

      Enables page domain notifications.

      https://developer.chrome.com/devtools/docs/protocol/1.1/page
      #command-enable

   navigate()

      Navigates current page to the given URL.

      https://developer.chrome.com/devtools/docs/protocol/1.1/page
      #command-navigate

   relaod()

      Reloads given page optionally ignoring the cache.

      https://developer.chrome.com/devtools/docs/protocol/1.1/page
      #command-reload

   set_geolocation_override()

      Overrides the Geolocation Position or Error.

      https://developer.chrome.com/devtools/docs/protocol/1.1/page
      #command-setGeolocationOverride


chromedevtools.runtime module
=============================

Runtime

Runtime domain exposes JavaScript runtime by means of remote
evaluation and mirror  objects. Evaluation results are returned as
mirror object that expose object type, string  representation and
unique identifier that can be used for further object reference.
Original  objects are maintained in memory unless they are either
explicitly released or are released  along with the other objects in
their object group.

https://developer.chrome.com/devtools/docs/protocol/1.1/runtime

class class chromedevtools.runtime.Runtime(websocket_connection)

   Bases: "chromedevtools.mixins.CreateCommand",
   "chromedevtools.mixins.ReceiveData"

   call_function_on()

      Calls function with given declaration on the given object.
      Object group of the result is inherited  from the target object.

      https://developer.chrome.com/devtools/docs/protocol/1.1/runtime
      #command-callFunctionOn

   enable()

      Enables reporting of execution contexts creation by means of
      executionContextCreated  event. When the reporting gets enabled
      the event will be sent immediately for each existing  execution
      context.

      https://developer.chrome.com/devtools/docs/protocol/1.1/runtime
      #command-enable

   evaluate(expression)

      Evaluates expression on global object.

      https://developer.chrome.com/devtools/docs/protocol/1.1/runtime
      #command-getProperties

   get_properties(object_id)

      Returns properties of a given object. Object group of the result
      is inherited from the target  object.

      https://developer.chrome.com/devtools/docs/protocol/1.1/runtime
      #command-getProperties

   release_object()

      Releases remote object with given id.

      https://developer.chrome.com/devtools/docs/protocol/1.1/runtime
      #command-releaseObject

   release_object_group()

      Releases all remote objects that belong to a given group.

      https://developer.chrome.com/devtools/docs/protocol/1.1/runtime
      #command-releaseObjectGroup


chromedevtools.timeline module
==============================

Timeline

Timeline provides its clients with instrumentation records that are
generated during the page  runtime. Timeline instrumentation can be
started and stopped using corresponding  commands. While timeline is
started, it is generating timeline event records.

https://developer.chrome.com/devtools/docs/protocol/1.1/timeline

class class chromedevtools.timeline.Timeline(websocket_connection)

   Bases: "chromedevtools.mixins.CreateCommand",
   "chromedevtools.mixins.ReceiveData"

   start()

      Starts capturing instrumentation events.

      https://developer.chrome.com/devtools/docs/protocol/1.1/timeline
      #command-start

   stop()

      Stops capturing instrumentation events.

      https://developer.chrome.com/devtools/docs/protocol/1.1/timeline
      #command-stop


Module contents
===============

class class chromedevtools.ChromeDevTools(websocket_url)

   Bases: "chromedevtools.mixins.CreateCommand",
   "chromedevtools.mixins.ReceiveData"

   Docstring for class ChromeDevTools.

   click(x, y)

   close()

   evaluate(expression)

   get_clickable()

   get_dom()

   get_scrollable()

   type(text)
