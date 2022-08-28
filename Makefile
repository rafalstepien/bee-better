lint:
	black . && isort . && flake8


test:
	pytest bee_better/


run-coverage:
	coverage run -m pytest bee_better/tests/


get-coverage-report:
	coverage html


open-coverage-report:
	google-chrome htmlcov/index.html


coverage: run-coverage get-coverage-report open-coverage-report
