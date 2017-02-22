#Follows the following style guide http://clarkgrubb.com/makefile-style-guide
MAKEFLAGS += --warn-undefined-variables
.DELETE_ON_ERROR:
.SUFFIXES:


python :=venv/bin/python3

pip-install :=build/pip-install

${python}:
	virtualenv -p python3 venv

${pip-install}: ${python} requirements.txt
	venv/bin/pip3 install -r requirements.txt
	touch ${pip-install}

.PHONY: run
run:
	${python} source/parser.py input/hello_world.txt

#.PHONY: check
#check:

.PHONY: install
install: ${pip-install}

.PHONY: clean
clean:
	rm -rf venv
