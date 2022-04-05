## rodar lints
.PHONY: lint, style, formatter, isort
lint:
	pylint main.py
	pylint config.py
	pylint ./app
style:
	pycodestyle main.py
	pycodestyle config.py
	pycodestyle ./app
isort:
	isort main.py
	isort config.py
	isort ./app
formatter:	isort
	blue main.py
	blue config.py
	blue ./app
