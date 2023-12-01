#! /bin/bash

set -o errexit   # abort on nonzero exitstatus
set -o nounset   # abort on unbound variable
set -o pipefail  # don't hide errors within pipes

sum=0
while IFS= read -r line; do
  numbers="${line//[!0-9]/}"
  pair="$(echo $numbers | cut -c 1)$(echo $numbers | cut -c ${#numbers})"
  sum=$(( $sum + $pair ))
done < ${1}
echo $sum
