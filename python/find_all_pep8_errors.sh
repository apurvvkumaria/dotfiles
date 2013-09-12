#! /bin/bash


# cd to the project

find . -iname "*.py" | grep ".*\.py$" | xargs pep8 --exclude=setup.py  > pep8_errors.log; awk '/.*E[0-9]+.*/' pep8_errors.log; rm pep8_errors.log
