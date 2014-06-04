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