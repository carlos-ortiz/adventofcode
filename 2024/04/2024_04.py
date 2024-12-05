# https://adventofcode.com/2024/day/4
import numpy as np

# https://www.geeksforgeeks.org/searching-in-a-numpy-array/
def check_horizontal(data):
  match=np.matrix(['X', 'M', 'A', 'S'],dtype=str)
  for row in data:
    match = np.matrix(['X', 'M', 'A', 'S'])
    if match in row:
      print(row)
    a=np.searchsorted(row,match,side="left")
    b=np.searchsorted(row,match,side="right")
    print(row)

  return 0
def check_vertical(data):
  return 0
def check_diagonal(data):
  return 0


if __name__ == '__main__':
  part1=0
  part2=0

  tmp=np.loadtxt("2024_04_test.dat", dtype=str)
  data=np.empty(shape=(len(tmp), len(tmp)), dtype=str)

  for item,value in enumerate(tmp):
    data[item,:]=list(value)

  part1+=check_horizontal(data)
  part1+=check_vertical(data)
  part1+=check_vertical(data)



  print("--- RESULT ---")
  print(part1)
  print(part2)
