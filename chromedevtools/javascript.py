from __future__ import absolute_import, division, print_function, unicode_literals

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

IS_ELEMENT_CLICKABLE = lambda(xpath) : """
    el = document.evaluate(%s, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
    if (el.href != null || el.onclick === "function") true;
    else false;
""" % xpath

IS_ELEMENT_SCROLLABLE = lambda(xpath) : """
    el = document.evaluate(%s, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
    if  ((el.scrollHeight > el.clientHeight || el.scrollWidth > el.clientWidth) && 
         (el.style.overflow != "hidden") 
        ) true;
    else false;
""" % xpath
