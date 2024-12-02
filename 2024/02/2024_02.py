import numpy
import numpy as np
from libxml2 import newTextLen
from numpy import dtype

if __name__ == '__main__':
  part1=0
  part2=0

  with (open("2024_02_test.dat", "r") as fp):
    for line in fp:
      data=np.fromiter(line.split(), dtype=int)

      data_len=len(data)-1
      data_diff=np.diff(data)
      data_diff_sign=np.sign(data_diff)

      # Levels are either increasing or decreasing (by at least one)
      equal_sign=abs(sum(data_diff_sign)) == data_len
      # Any two adjacent levels differ by at most three
      two_adjacent_less_than_three=all(abs(data_diff) < 4)

      # At least all but one level are either increasing or decreasing (by at least one)
      almost_equal_sign=abs(sum(data_diff_sign)) < data_len

      if equal_sign and two_adjacent_less_than_three:
        part1+=1

      if almost_equal_sign:
        if 0 in data_diff_sign:
          testdata = numpy.delete(data, np.where(data_diff_sign == 0))
#          print(testdata)

          testdata_len = len(testdata)-1
          testdata_diff = np.diff(testdata)
          testdata_diff_sign = np.sign(testdata_diff)

          # Levels are either increasing or decreasing (by at least one)
          test_equal_sign = abs(sum(testdata_diff_sign)) == testdata_len
          # Any two adjacent levels differ by at most three
          test_two_adjacent_less_than_three = all(abs(testdata_diff) < 4)

          if test_equal_sign and test_two_adjacent_less_than_three:
            part2 += 1

#      print(data)

#        print("---")

  print("--- RESULT ---")
  print(part1)
  print(part2)
