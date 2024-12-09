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


import re

def check_line(sub, my_line):
  forward=re.findall(sub, my_line)
  backward = re.findall(sub, my_line[::-1])

  return len(forward) + len(backward)


if __name__ == '__main__':
  part1=0
  part2=0

  teststr="XMAS"

  adata = np.loadtxt("2024_04.dat", dtype=str)

  mdata = np.empty([len(adata), len(adata[0])], dtype=str)
  mdim=mdata.ndim
  mshape=mdata.shape
  for i,line in enumerate(adata):
    for j,item in enumerate(line):
      mdata[i,j] = item
  tdata=mdata.transpose()

  for i, mdatum in enumerate(mdata):
    row=mdata[i]
    col=mdata.transpose()[i]
    diag1=np.diagonal(mdata, i)
    diag2=np.diagonal(mdata.transpose(), i)
    diag3=np.diagonal(np.fliplr(mdata), i)
    diag4=np.diagonal(np.fliplr(mdata).transpose(), i)

    part1 += check_line(teststr, "".join(row))
    part1 += check_line(teststr, "".join(col))

    part1 += check_line(teststr, "".join(diag1))
    part1 += check_line(teststr, "".join(diag3))

    if i != 0:
      part1 += check_line(teststr, "".join(diag2))
      part1 += check_line(teststr, "".join(diag4))


  tmp=np.loadtxt("2024_04_test.dat", dtype=str)
  data=np.empty(shape=(len(tmp), len(tmp)), dtype=str)

  for item,value in enumerate(tmp):
    data[item,:]=list(value)

#  part1+=check_horizontal(data)
#  part1+=check_vertical(data)
#  part1+=check_vertical(data)



  print("--- RESULT ---")
  print(part1)
  print(part2)
