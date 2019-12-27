#!/bin/bash

: '
Author: Alexander Zsikla
Date: 12/27/19
unittest.sh

Description: Tests all of the modules
'

for file in `ls test*`; do
	echo -e "\n$file BEING TESTED"
	python3 $file || echo -e "Test in $file Failed!"
	echo ""
done