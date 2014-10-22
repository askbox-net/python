#!/bin/bash

run(){
	filename=$1
	echo "-- start --"
	python $filename
	echo "-- end --"
}

inotifywait -mrq -e modify --format '%w%f' $PWD |
while read line
do
	if [[ $line =~ .*\.py$ ]]; then
		run $line
	fi
done

