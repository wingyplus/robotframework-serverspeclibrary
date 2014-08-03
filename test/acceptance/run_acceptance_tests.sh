#!/bin/sh

export PYTHONPATH="`pwd`/src"

vagrant up --provision
pybot ./test/acceptance/
vagrant halt
