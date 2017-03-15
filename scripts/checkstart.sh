#!/bin/bash

## checkstart.sh
# Determine if the scripts are running.
# By Anton Foltz

result=`ps aux | grep -i "watch.py" | grep -v "grep" | wc -l`
if [ $result -ge 1 ]
   then
        exit 1
   else
        /home/pi/pi-detector/watch.sh start > /dev/null &
fi

result=`ps aux | grep -i "pi-timolo.py" | grep -v "grep" | wc -l`
if [ $result -ge 1 ]
   then
        exit 1
   else
        /home/pi/pi-timolo/pi-timolo.sh start > /dev/null &
fi

exit 0
