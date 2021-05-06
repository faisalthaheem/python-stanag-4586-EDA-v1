#!/bin/sh
python setup.py bdist
/var/data/python/bin/twine upload --repository pypi dist/* --verbose