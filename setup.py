import sys
from distutils.core import setup

REQUIRES = [
    'cssselect==0.9.1',        
    'lxml==3.3.4',        
    'requests==2.3.0',
    'six==1.6.1',
]

if sys.version_info >= (3,):
    REQUIRES.append('websocket-client==0.15.0')
elif sys.version_info >= (2,6):
    REQUIRES.append('websocket-client-py3==0.15.0')

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