try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='lizepy',
    version='0.2.0',
    author='Alexandre Vicenzi',
    author_email='vicenzi.alexandre@gmail.com',
    packages=['lizepy'],
    url='https://github.com/alexandrevicenzi/lizepy',
    license='LICENSE',
    description='Python lib for Telize JSON IP and GeoIP REST API',
    install_requires=[
        "iptools >= 0.6.1"
    ]
)
