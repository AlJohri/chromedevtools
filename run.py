import sys

from chromedevtools import ChromeDevTools

POSITION_ELEMENTS = ['offsetParent', 'offsetLeft', 'offsetTop', 'scrollLeft', 'scrollTop', 'clientLeft', 'clientTop', 'clientWidth', 'clientHeight']

with ChromeDevTools(sys.argv[1]) as cdt:

    # dom = cdt.get_dom()
    # els1 = cdt.get_clickable()
    # els2 = cdt.get_scrollable()

    ret2 = cdt.type("asdfasdf")
    ret1 = cdt.click(0, 0)
    

    # print(dom)
    # print(els1)
    # print(els2)
    print(ret1)
    print(ret2)