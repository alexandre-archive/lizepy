try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='pylize',
    version='0.2.0',
    author='Alexandre Vicenzi',
    author_email='vicenzi.alexandre@gmail.com',
    packages=['pylize'],
    url='https://github.com/alexandrevicenzi/pylize',
    license='LICENSE',
    description='Python lib for Telize JSON IP and GeoIP REST API',
    install_requires=[
        "iptools >= 0.6.1"
    ]
)
