lint:
	black . && isort . && flake8


test:
	pytest bee_better/
