#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  File: Triangle.py

#  Description: The following program finds the greatest path sum using different methods.

#  Student Name: Gaytri Riya Vasal

#  Course Name: CS 313E

#  Unique Number: 51120

#  Date Created: 3/2/22

#  Date Last Modified: 3/4/22

import sys

from timeit import timeit

# returns the greatest path sum using exhaustive search
def brute_force (grid):
    # base case: calculates the max path of a triangle with two rows
    if len(grid) == 2:
        return max(grid[1][0], grid[1][1]) + grid[0][0]
    else:
        # adds max of two elements to the next row of same index
        for i in range(len(grid[-1]) - 1):
            grid[len(grid) - 2][i] += max(grid[len(grid) - 1][i], grid[len(grid) - 1][i+1])
        # moves up grid by 1 row
        return brute_force(grid[:-1])
            

# returns the greatest path sum using greedy approach
def greedy (grid):
    sum_grid = grid[0][0]
    current_col = 0
    # start from top to bottom
    for i in range(1, len(grid)):
        # shifts to left index
        if grid[i][current_col] > grid[i][current_col + 1]:
            max_val = grid[i][current_col]
        # shifts to right index
        else:
            max_val = grid[i][current_col + 1]
            current_col += 1
        # increases sum by max val btwn 2
        sum_grid += max_val
       
    return sum_grid

# returns the greatest path sum using divide and conquer (recursive) approach
def divide_conquer (grid):
    # break up triangles into smaller triangles until you get to a triangle of 
    # 2 rows; find the max path of triangles compare the paths 
    
    # will return a single number as the sum
    return divide_conquer_helper (grid, 0, 0, 0)

def divide_conquer_helper (grid, row, col, sum):

    # to avoid row from getting out of range
    if row == len(grid) - 1:

        # adds to the sum
        return grid[row][col]

    else:

        #adds to the sum
        return grid[row][col] + max(divide_conquer_helper(grid, row + 1, col, sum),  divide_conquer_helper(grid, row + 1, col + 1, sum))
        

# returns the greatest path sum and the new grid using dynamic programming
def dynamic_prog (grid):
    for i in range(len(grid) - 1, 0, -1):
        for j in range(len(grid[i]) - 1):
            # adds max top value to value of row lower
            grid[i-1][j] +=  max(grid[i][j], grid[i][j+1])
            
    return grid[0][0]

# reads the file and returns a 2-D list that represents the triangle
def read_file ():
  # read number of lines
  line = sys.stdin.readline()
  line = line.strip()
  n = int (line)

  # create an empty grid with 0's
  grid = [[0 for i in range (n)] for j in range (n)]

  # read each line in the input file and add to the grid
  for i in range (n):
    line = sys.stdin.readline()
    line = line.strip()
    row = line.split()
    row = list (map (int, row))
    for j in range (len(row)):
      grid[i][j] = grid[i][j] + row[j]

  return 

def main ():
  # read triangular grid from file
  grid = read_file()
  
  '''
  # check that the grid was read in properly
  print (grid)
  '''

  # output greatest path from exhaustive search
  times = timeit ('brute_force({})'.format(grid), 'from __main__ import brute_force', number = 10)
  times = times / 10
  # print time taken using exhaustive search

  # output greatest path from greedy approach
  times = timeit ('greedy({})'.format(grid), 'from __main__ import greedy', number = 10)
  times = times / 10
  # print time taken using greedy approach

  # output greatest path from divide-and-conquer approach
  times = timeit ('divide_conquer({})'.format(grid), 'from __main__ import divide_conquer', number = 10)
  times = times / 10
  # print time taken using divide-and-conquer approach

  # output greatest path from dynamic programming 
  times = timeit ('dynamic_prog({})'.format(grid), 'from __main__ import dynamic_prog', number = 10)
  times = times / 10
  # print time taken using dynamic programming

if __name__ == "__main__":
  main()

