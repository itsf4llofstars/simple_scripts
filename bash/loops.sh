#!/usr/bin/bash

iters=0

while [ $iters -lt 10 ]; do
   printf "%s\n" "Iters: $iters"
   iters=$(($iters + 1))
done

echo

until [ $iters -eq 0 ]; do
   printf "%s\n" "Iters: $iters"
   iters=$(($iters - 1))
done

echo

for var in bacon butter beans
do
   printf "%s\n" "Word: $var"
done

echo

for (( n=0; n<=10; ++n ))
do
   printf "%s\n" "n = $n"
done

echo

for n in a b c
do
    echo "$n"

    while true
    do
        rand=$RANDOM
        echo "$rand"

        if [ "$rand" -gt 20000 ]
        then
            break 2
        elif [ "$rand" -lt 10000 ]
        then
            break
        fi
    done

    sleep 3
done

echo

exit 0
