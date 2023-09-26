install:
	poetry install

lint:
	poetry run flake8 gendiff

build:
	poetry build

package-install:
	python3 -m pip install --user dist/*.whl

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

test:
	poetry run pytest

selfcheck:
	poetry check

check: selfcheck test lint