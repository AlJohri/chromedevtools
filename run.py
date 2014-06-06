import sys, six, lxml.etree

if six.PY2:
    import __builtin__
    input = getattr(__builtin__, 'raw_input')

from chromedevtools import ChromeDevTools

POSITION_ELEMENTS = ['offsetParent', 'offsetLeft', 'offsetTop', 'scrollLeft', 'scrollTop', 'clientLeft', 'clientTop', 'clientWidth', 'clientHeight']

with ChromeDevTools(sys.argv[1]) as cdt:

    dom = cdt.get_dom()
    tree = lxml.etree.ElementTree(dom)
    for e in dom.iter():
        xpath = tree.getpath(e)
        print xpath, cdt.check_clickable(xpath), cdt.check_scrollable(xpath)

    els1 = cdt.get_clickable()
    els2 = cdt.get_scrollable()

    print(els1)
    print(els2)

    ret1 = cdt.type("asdfasdf")
    ret2 = cdt.click(0, 0)
    
    print(ret1)
    print(ret2)

    color = {'r': 255, 'g': 0, 'b': 0}
    ret3 = cdt.dom.highlight_rect(10,10,100,100,color)

    input(
        "Alt-Tab to your Chrome Browser and see the highlighted rectangle." +
        "Then, press Enter to terminate."
    )

    print(ret3)