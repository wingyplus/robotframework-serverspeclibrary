#!/bin/sh

export PYTHONPATH=`pwd`

vagrant up
pybot ./test/acceptance/command.robot
vagrant halt
