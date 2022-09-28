poetry-install:
	poetry install
	poetry run pre-commit install
	poetry shell

pip-install:
	python3 -m pip install -r build/requirements.txt
	pre-commit install

poetry-requirements:
	poetry export --with dev --without-hashes --format=requirements.txt > build/requirements.txt

pip-requirements:
	pip freeze > build/requirements.txt
