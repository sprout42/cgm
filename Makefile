PYTHON_VERSION ?= $(shell python3.8 -c 'import sys; print(sys.executable)' 2> /dev/null)
ifeq ($(shell which "$(PYTHON_VERSION)"),)
$(error python3.8 not found, please install and try again)
endif

PYTHON_VERSION_CHECK := $(shell python -c "import sys; assert sys.version_info.major == 3 and sys.version_info.minor >= 8")
ifneq ($(shell which "$(PYTHON_VERSION_CHECK)"),)
$(error python version needs to be at least 3.8)
endif

.PHONY: all wheel install uninstall scrape-standard test clean

# Some vars to keep track of things
BUILD := build
DIST := dist
PKG := cgm
VER := 0.9
WHEEL := $(DIST)/$(PKG)-$(VER)-py3-none-any.whl

all: wheel

build:
	python setup.py build

$(WHEEL): build
	python setup.py bdist_wheel

wheel: $(WHEEL)

install: build
	pip install --force-reinstall $(WHEEL)

uninstall:
	pip uninstall -y cgm

utils/env:
	virtualenv -p $(PYTHON_VERSION) utils/env
	. utils/env/bin/activate && python -m pip install --upgrade pip
	. utils/env/bin/activate && pip install -r utils/requirements.txt

scrape-standard: utils/env
	. utils/env/bin/activate && ./utils/make_cgm_types.py docs/c032380e.pdf cgm/types/parsed_types.py

test:
	@echo "TODO" && false

clean:
	rm -rf utils/env
	rm -rf build
	rm -rf dist
	rm -rf cgm.egg-info
