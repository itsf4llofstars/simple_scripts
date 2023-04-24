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

exit 0
