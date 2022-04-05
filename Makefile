## rodar lints
.PHONY: lint
lint:
	pylint main.py
	pylint ./app