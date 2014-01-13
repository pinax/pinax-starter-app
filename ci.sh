set -e

export DJANGO_SETTINGS_MODULE=tests.settings
export PYTHONPATH=.

flake8 {{ app_name }} --ignore=E501 --max-complexity=10 --statistics --benchmark
coverage run --branch --source={{ app_name }} `which django-admin.py` test tests
coverage report
