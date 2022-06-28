# Algorithm Notes

Notes taken as I read thru the book Grokking Algorithms by Aditya Y. Bhargava

## Big O Notation

- It's not enough to know how long an algorithm takes to run. You need to know how the running time increases as the list
size increases! 
- For example, simple search entails linear time, but binary search entails log time.  
- Big O doesn't tell you the speed in seconds-- it lets you compare the number of operations. It tells you
how fast the algorithm grows.  
- Big O always assumes the worst case scenario, the maximum number of operations it would take to finish.  
- Logs are always expressed in base 2 and n is the number of operations.  
  
>&nbsp;&nbsp; Common Big O run times:  
>&nbsp;&nbsp; O(log n)-- log time, ex. Binary Search  
>&nbsp;&nbsp; O(n)-- linear time, ex. Simple search  
>&nbsp;&nbsp; O(n * log n)-- ex. A fast sorting algorithm, like quicksort  
>&nbsp;&nbsp; O(n**2)-- ex. A slow sorting algorithm, like selection sort  
>&nbsp;&nbsp; O(n!)-- factorial time, ex. A really slow algorithm, like traveling salesperson.  
  
## Binary Search  

- Useful when you have a list in sorted order. 
- For an ordered list of n items, in a worst case scenario, it will take binary search log2n steps to run.  
- Speed: O(log n)  

```python
def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess < item:
            low = mid + 1
        elif guess > item:
            high = mid - 1
        
my_list = [1,3,5,7,9]
print(binary_search(my_list, 10))
```  

## The Traveling Salesperson

Example - you have a salesperson that has to visit 5 cities, but wants to
minimize travel time. To do this, every travel permutation must be considered
and from that, the lowest travel distance selected.  
  
There is no known way to solve this faster.

Speed(n!) - Factorial time
This becomes exceedingly slow as the list grows. For 15 cities, it would take 1.3 
TRILLION operations. 

