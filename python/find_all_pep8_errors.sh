#! /bin/bash


# cd to the project

find . -iname "*.py" | grep ".*\.py$" | xargs pep8 --exclude=setup.py  > test.log; awk '/.*E[0-9]+.*/' test.log; rm test.log
