import sys
from distutils.core import setup

REQUIRES = [
    'cssselect',
    'lxml',        
    'requests',
    'six',
]

if sys.version_info >= (3,):
    REQUIRES.append('websocket-client')
elif sys.version_info >= (2,6):
    REQUIRES.append('websocket-client-py3')

setup(
    name='chromedevtools',
    version='0.0.1',
    description='Python Wrapper for Chrome DevTools',
    author='Al Johri',
    author_email='al.johri@mgail.com',
    url='https://github.com/AlJohri/chromedevtools',
    packages=['chromedevtools'],
    install_requires=REQUIRES
)
