# https://adventofcode.com/2024/day/5
import array
import sys
from typing import Type

import numpy as np
from qubesadmin.tools.qvm_firewall import rules_add


def with_iter(iterable):
  with iterable as iterator:
    yield from iterator


def find_index(iterable: list, my_value: str) -> int:
  try:
    return iterable.index(my_value)
  except ValueError:
    return -1

def check_order(order: list, my_list: list) -> Type[ValueError] | bool:
  if len(order) != 2:
    return ValueError
  return False
#  return find_index(my_list, order[0]) < find_index(my_list, order[1]) # check != -1

if __name__ == '__main__':
  part1=0
  part2=0

  rules = []
  updates = []

  for line in with_iter(open('2024_05_test.dat')):
    "".join(line).strip()
    if '|' in line:
      rules.append("".join(line).strip().split('|'))
    if ',' in line:
      updates.append("".join(line).strip().split(','))

  rules_sorted = sorted(rules)

  hits = []
  for i, line in enumerate(updates):
    for j, item in enumerate(line):
      indices = [x for x, rule in enumerate(rules) if item in rule]
      for k in range(len(indices)):
        before = rules[k][0]
        after  = rules[k][1]
        order = [before, after]
        if before == after:
          print("WARNING")

        if item in order:
          check_order(item, line, order)

          l=find_index(line, before)
          m=find_index(line, after)


          if l < m:
            part1 += 1



  print("--- RESULT ---")
  print(part1)
  print(part2)
