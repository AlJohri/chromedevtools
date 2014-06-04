import sys

from chromedevtools import ChromeDevTools

POSITION_ELEMENTS = ['offsetParent', 'offsetLeft', 'offsetTop', 'scrollLeft', 'scrollTop', 'clientLeft', 'clientTop', 'clientWidth', 'clientHeight']

with ChromeDevTools(sys.argv[1]) as cdt:

    dom = cdt.get_dom()
    print(dom)

    els1 = cdt.get_clickable()
    els2 = cdt.get_scrollable()

    print(els1)
    print(els2)

    ret1 = cdt.type("asdfasdf")
    ret2 = cdt.click(0, 0)
    
    print(ret1)
    print(ret2)