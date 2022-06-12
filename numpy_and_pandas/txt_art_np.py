# This is an alternate solution to the DMOJ challenge, coci19c5p1,
# using the numpy library.

# Daniel is making some text art in a text editor.
# The pictures will consist of even rows of '.' and '*'.
# The * characters will form non-overlapping rectanles.
# The rectangles will also not touch each other on any of 
# their surfaes. 
# Write a program to count the number of rectangles Daniel drew.

# Input:
# First line: N number of rows, M number of characters per row.
# Following lines - the sequences of . and *

# Output: 
# The number of rectangles drawn

# My approach:
# Given the contraints of the rectangles, each one will necessarily
# have an upper left corner that is not directly adjecent to another
# * charater to the immediate left and above.
# Scan each character to see if it's a '*' and if it meets that 
# that criteria, and if so, increment the rectangle count.
# (I added in a row and column of only . characters to make this easier).

import numpy as np

# collect inputs for the number of rows and columns
x = input().split(' ')
lines = int(x[0])
chars = int(x[1])

# create the blank top row, and start the numpy array
first_row = []
for i in range(chars+1):
    first_row.append('.')
grid = np.array(first_row)

# collect inputs for the character sequences preceding each with a '.' to 
# make a blank column. Then append each of these rows to the array
for line in range(lines):
    row = ['.']
    for char in input():
        row.append(char)
    grid = np.vstack([grid, row]) 

# iterate thru the cells and test for * characters with a . directly above and to the left    
rectangles = 0
for idx, cell in np.ndenumerate(grid):
    x, y = idx
    if cell == "*" and grid[(x-1), y] == '.' and grid[x,(y-1)] == '.':
        rectangles += 1

print(rectangles)    
    




