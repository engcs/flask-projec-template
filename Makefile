## rodar lints
.PHONY: lint, style
lint:
	pylint main.py
	pylint config.py
	pylint ./app
style:
	pycodestyle main.py
	pycodestyle config.py
	pycodestyle ./app