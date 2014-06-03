import sys

from chromedevtools import ChromeDevTools

JS_FIND_CLICKABLE_ELEMENTS = """
ret = []; 
els = document.getElementsByTagName("*"); 
for(var i=0; i < els.length; i++) { 
    el = els[i]; if (el.href != null) 
        ret.push(el); 
    else if (el.onclick === "function") 
        ret.push(el); 
} 
ret
"""

JS_FIND_SCROLLABLE_ELEMENTS = """
ret = []; 
els = document.getElementsByTagName("*"); 
for(var i=0; i < els.length; i++) { 
    el = els[i]; 
    if  ((el.scrollHeight > el.clientHeight || el.scrollWidth > el.clientWidth) && 
         (el.style.overflow != "hidden") 
        )
        ret.push(el); 
} 
ret    
"""

POSITION_ELEMENTS = ['offsetParent', 'offsetLeft', 'offsetTop', 'scrollLeft', 'scrollTop', 'clientLeft', 'clientTop', 'clientWidth', 'clientHeight']

with ChromeDevTools(sys.argv[1]) as cdt:

    doc = cdt.dom.get_document()
    root_id = doc['root']['nodeId']
    dom = cdt.dom.get_outer_html(root_id)['outerHTML']

    ret_clickable = cdt.runtime.evaluate(JS_FIND_CLICKABLE_ELEMENTS)
    remote_object = ret_clickable['objectId']
    if ret_clickable['className'] == "Array":
        object_properties = cdt.runtime.get_properties(remote_object)
        elements = list(filter(lambda prop: prop['name'].isdigit(), object_properties))

    for el in elements:
        print(el)

    ret_scrollable = cdt.runtime.evaluate(JS_FIND_SCROLLABLE_ELEMENTS)
    