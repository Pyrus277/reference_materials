## Working with file objects in Python

Open the specified file object. The second argumnent is 'r' by default. Other options:    
```python
with open('test.txt', 'r') as fhand:
    #^If you work outside the indent, you'll still have access
    #to the fhand variable, it'll just be closed. 
```
'w' - Opens file for writing. Will overrite. Works like $ touch
'w+' - Write and read  
'a' - Append. Like 'w', but will not overwrite  
'r' - Read only. If you omit the argument, this is default.  
'r+' - Open for reading and writing (not sure how this differs from 'w+')  
'a+' - Append and read.  
  

.readline() - similar to input() except it takes from a file instead of user.

.rstrip() removes whitespace and newline char. 

.readlines() - puts each line into a list
