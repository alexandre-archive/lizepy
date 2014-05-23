all: build install test

build:
	python setup.py build

install:
	sudo python setup.py install

test:
	python -m unittest -v tests.test