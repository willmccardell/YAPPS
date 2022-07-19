#!/usr/bin/sh

pip install --editable .[test]

echo "Linting...."
flake8 --max-line-length=88 tests yapps

echo "Testing..."
pytest