.DEFAULT_GOAL := all

isort:
	poetry run isort -c setup.cfg

black:
	poetry run black --line-length=120 --target-version py38 troopy

mypy:
	poetry run mypy troopy

test:
	poetry run pytest

lint:
	poetry run isort -c setup.cfg
	poetry run black --line-length=120 --target-version py38 troopy
	poetry run mypy troopy

all:
	poetry run isort -c setup.cfg
	poetry run black --line-length=120 --target-version py38 troopy
	poetry run mypy troopy
	poetry run pytest

build:
	poetry run isort -c setup.cfg
	poetry run black --line-length=120 --target-version py38 troopy
	poetry run mypy troopy
	poetry run pytest
	poetry build

publish:
	poetry publish --build
