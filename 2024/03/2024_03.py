# https://adventofcode.com/2024/day/3

import re
if __name__ == '__main__':
  part1=0
  part2=0

  with (open("2024_03.dat", "r") as fp):
    for line in fp:
      mul=re.findall(r'(mul\(\d{1,3},\d{1,3}\))', line)
      for val in mul:
        v=re.sub(r'[mul()]','',val).split(',')
        part1+=int(v[0])*int(v[1])

  print("--- RESULT ---")
  print(part1)
#  print(part2)
