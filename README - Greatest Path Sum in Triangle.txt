
PROJECT DESCRIPTION AND GUIDELINES PROVIDED ON ASSIGNMENT INSTRUCTIONS

This assignment is a variation of a problem from Project Euler. You are required to find the greatest path sum starting at the top of the triangle and moving only to adjacent numbers on the row below.

   3
  7 4
 2 4 6
8 5 9 3

In the above triangle, the maximum path sum is 3 + 7 + 4 + 9 = 23.

You will read your input from the file triangle.in. The first line indicates n the number of rows in the triangle. This will be followed by n lines of data. Each line of data will have only positive integers greater than 0. The first line of data in the triangle will have one number, the second line in the triangle will have two numbers and so on. The nth line will have n integers.

You will apply four different approaches to problem-solving to this single problem - exhaustive search (recursive), greedy, divide and conquer (recursive), and dynamic programming. The functions - brute_force(), greedy(), divide_conquer(), and dynamic_prog() are wrapper functions. You must use the grid returned from calling the read_file() function. You cannot change the header of any of the given functions, but you can always add more helper functions.

Both the exhaustive search and the divide and conquer methods are recursive. Here is the difference. In the exhaustive search, you will store all the path sums. You will then find the maximum from all the path sums. In the divide and conquer method, you will only get back a single number that is the maximum path sum. The exhaustive search will give you a lot more information if you need it. For example, you can get the minimum, mean, median, standard deviation, and frequency distribution of the path sums. The amount of time taken to do the exhaustive search and the divide and conquer should be about the same. The exhaustive search may be a tad longer.

You will have these lines of output:

The greatest path sum through exhaustive search is 
23
The time taken for exhaustive search in seconds is
x

The greatest path sum through greedy search is 
23
The time taken for greedy approach in seconds is
x

The greatest path sum through recursive search is 
23
The time taken for recursive search in seconds is
x

The greatest path sum through dynamic programming is 
23
The time taken for dynamic programming in seconds is
x

Most likely, the maximum path that you will get from exhaustive search, recursive search, and dynamic programming will be the same. On the other hand, the result from the greedy search will be less, and so will the execution time.

To run this code on the command line on Mac, you will do:

python3 Triangle.py < triangle.in

To run the code on the command line on a Windows machine, you will do:

python Triangle.py < triangle.in

