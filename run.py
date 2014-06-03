import sys

from chromedevtools import ChromeDevTools

cdt = ChromeDevTools(sys.argv[1])
doc = cdt.dom.get_document()
print(doc)

# cdt.runtime.evaluate("alert('hello world!');")