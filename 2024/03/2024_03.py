# https://adventofcode.com/2024/day/3

import re
if __name__ == '__main__':
  part1=0
  part2=0

  with (open("2024_03_test.dat", "r") as fp):
    for line in fp:
      print(line)
      print(re.sub(r'[^mul(1-999,1-999)]', ' ', line))


  print("--- RESULT ---")
  print(part1)
  print(part1)
