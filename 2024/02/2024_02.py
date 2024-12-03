# https://adventofcode.com/2024/day/2

import numpy as np
from statistics import median


def get_diff(result):
  return np.diff(result)


def diff_sign(diff):
  return np.sign(diff)


def check_result(result):
  diff=get_diff(result)
  sign=diff_sign(diff)

  all_same_sign=abs(sum(sign))==len(diff) # Includes 0 in diff
  at_least_three=all(abs(diff)<4)         # Differs by at least three

  if all_same_sign and at_least_three:
    return True

  return False


def check_result_corr(result):
  diff=get_diff(result)
  sign=diff_sign(diff)
  ms=median(sign)

  if abs(sum(sign))!=len(diff):
    if abs(sum(sign))==len(diff)-1: # Two identical adjacent levels
      return check_result(np.delete(result,np.where(sign==0)))
    if abs(sum(sign))==len(diff)-2: # Two adjacent levels are not increasing/decreasing
     return check_result(np.delete(result,np.where(sign!=ms)))
    if any(diff>3):                 # Two adjacent levels differ by more than 3
      return check_result(np.delete(result,np.where(diff>3)))

  return False



if __name__ == '__main__':
  part1=0
  part2=0

  with (open("2024_02.dat", "r") as fp):
    for line in fp:
      data=np.fromiter(line.split(), dtype=int)
      if check_result(data):
        part1+=1

      if check_result_corr(data):
        part2+=1


  print("--- RESULT ---")
  print(part1)
  print(part1+part2)
