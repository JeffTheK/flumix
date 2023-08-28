.PHONY: cflumix

cflumix:
	g++ -o cflumix_app cflumix/*.cpp

install:
	pip install .

test: install
	pytest