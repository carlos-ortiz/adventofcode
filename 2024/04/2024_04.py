# https://adventofcode.com/2024/day/4

import re
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


def check_line(sub, my_line):
  forward=re.findall(sub, my_line)
  backward = re.findall(sub, my_line[::-1])

  return len(forward) + len(backward)

def check_mas(i, j, m):
  mas = "MAS"
  if i < 1 or i > 8:
    return 0
  if j < 1 or j > 8:
    return 0

  line_1 = m[i-1][j-1] + m[i][j] + m[i+1][j+1]
  line_2 = m[i-1][j+1] + m[i][j] + m[i+1][j-1]

  if mas in line_1 and mas in line_2:
    return 1
  if mas in line_1 and mas in line_2[::-1]:
    return 1
  if mas in line_1[::-1] and mas in line_2:
    return 1
  if mas in line_1[::-1] and mas in line_2[::-1]:
    return 1


  return 0

if __name__ == '__main__':
  part1=0
  part2=0

  xmas = "XMAS"
  mas = "MAS"

  adata = np.loadtxt("2024_04.dat", dtype=str)

  mdata = np.empty([len(adata), len(adata[0])], dtype=str)
  for i,line in enumerate(adata):
    for j,item in enumerate(line):
      mdata[i,j] = item

  for i, mdatum in enumerate(mdata):
    row=mdata[i]
    col=mdata.transpose()[i]
    diag1=np.diagonal(mdata, i)
    diag2=np.diagonal(mdata.transpose(), i)
    diag3=np.diagonal(np.fliplr(mdata), i)
    diag4=np.diagonal(np.fliplr(mdata).transpose(), i)

    part1 += check_line(xmas, "".join(row))
    part1 += check_line(xmas, "".join(col))

    part1 += check_line(xmas, "".join(diag1))
    part1 += check_line(xmas, "".join(diag3))

    if i != 0:
      part1 += check_line(xmas, "".join(diag2))
      part1 += check_line(xmas, "".join(diag4))


  all_x = np.where(mdata=='A')
  XX=all_x[0]
  YY=all_x[1]

  for i in range(len(XX)):
    part2 += check_mas(XX[i], YY[i], mdata)

  print("--- RESULT ---")
  print(part1)
  print(part2)
