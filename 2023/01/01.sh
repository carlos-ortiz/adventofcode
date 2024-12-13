#! /bin/bash

set -o errexit   # abort on nonzero exitstatus
set -o nounset   # abort on unbound variable
set -o pipefail  # don't hide errors within pipes

transform() {
  declare -A digits
  digits['one']='1'
  digits['two']='2'
  digits['three']='3'
  digits['four']='4'
  digits['five']='5'
  digits['six']='6'
  digits['seven']='7'
  digits['eight']='8'
  digits['nine']='9'

  for key in "${!digits[@]}"; do
    echo $key ${digits[$key]}
  done
}

main() {
  sum=0

  transform

  while IFS= read -r line; do
    numbers="${line//[!0-9]/}"
    pair="$(echo $numbers | cut -c 1)$(echo $numbers | cut -c ${#numbers})"
    echo $pair
    sum=$(( $sum + $pair ))
  done < ${1}
  echo $sum
}

main "$@"
