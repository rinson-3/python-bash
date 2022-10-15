#!/bin/bash

n=1
while [ $n -le 5 ]; do 
    echo "Iteration number $n"
    ((n+=1))
done


--------------------------------------

n=0
command=$1  # same as sys.argv[1] in python
while ! $command && [ $n -le 5 ]; do
    sleep $n 
    ((n=n+1))
    echo "Retry #$n"
done;
