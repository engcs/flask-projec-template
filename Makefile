## rodar lints
.PHONY: lint, style, formatter, isort
style:
	pycodestyle main.py
	pycodestyle config.py
	pycodestyle ./app
lint: style
	pylint main.py
	pylint config.py
	pylint ./app
isort:
	isort main.py
	isort config.py
	isort ./app
formatter:	isort
	blue main.py
	blue config.py
	blue ./app
