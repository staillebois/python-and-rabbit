PYTHON ?= python3.10

venv:
	@rm -rf venv
	@$(PYTHON) -m venv venv
	@. ./venv/bin/activate
	@pip install -r requirements.txt
	@echo "Virtual environment created"

test:
	@. ./venv/bin/activate
	@pytest

lint:
	@. ./venv/bin/activate
	@pylint **/*.py

.PHONY: venv test lint