# https://adventofcode.com/2024/day/3

import re

if __name__ == '__main__':
  part1=0
  part2=0
  dont = 'don\'t()'
  do = 'do()'

  mul=[]
  with (open("2024_03.dat", "r") as fp):
    for line in fp:
      tmp = re.findall(r'(mul\(\d{1,3},\d{1,3}\))', line)
      mul+=tmp
  for val in mul:
    v=re.sub(r'[mul()]','',val).split(',')
    part1+=int(v[0])*int(v[1])

  mul=[]
  with (open("2024_03.dat", "r") as fp):
    for line in fp:
      tmp = re.findall(r'(mul\(\d{1,3},\d{1,3}\)|don\'t\(\)|do\(\))', line)
      mul+=tmp

  for i in [index for index,value in enumerate(mul) if value==dont]:
    next_dont = next((index for index, value in enumerate(mul) if value == dont), len(mul))
    next_do = next((index for index, value in enumerate(mul) if index > next_dont and value == do), len(mul) - 1)
    for j in range(next_dont, next_do + 1):
      mul.pop(next_dont)

  for val in mul:
    if val!=do:
      v=re.sub(r'[mul()]','',val).split(',')
      part2+=int(v[0])*int(v[1])

  print("--- RESULT ---")
  print(part1)
  print(part2)
