install:
	poetry install

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest

selfcheck:
	poetry check

check: selfcheck test lint