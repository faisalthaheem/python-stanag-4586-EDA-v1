#!/bin/sh
python setup.py bdist
/var/data/python/bin/twine upload --repository testpypi dist/* --verbose