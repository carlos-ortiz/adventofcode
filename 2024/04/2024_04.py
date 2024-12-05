# https://adventofcode.com/2024/day/4
import numpy as np

if __name__ == '__main__':
  part1=0
  part2=0

  data=[]
  tmp=np.loadtxt("2024_04_test.dat",dtype=str)
  for i in range(len(tmp)):
    data.append(list(tmp[i]))
  print(data)

#  mdata=np.matrix(data,dtype=str)  # to int

  print("--- RESULT ---")
  print(part1)
  print(part2)
