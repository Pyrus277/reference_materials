# Data Structures

## Memory

Any time you want to store an item in memory, you ask
the computer to allocate some space for it. Each space has an
address. If you want to store multiple items, there are two
basic ways to do so: arrays and linked lists. 
Like with everything, they each have pros and cons, and it's 
important to know the differences.
Note: Python uses dynamic arrays which make arrays and linked lists
somewhat comparable in memory useage. (Read up on dynamic arrays in Python)

## Arrays

This stores all your items contiguously in memory.
But what if you add something to your array and the next spot
in memory is occupied? You need to ask your computer for a 
different chunk of memory that can fit the array of this new
length, and then move all the items there. If this happens again
you'll have to move a second time. 
One fix is to "hold spots"-- ask for 10 slots, even tho you only
currently need 3 (SQL).
But this has downsides: 
-Extra space can end up wasted if you don't fill it.
-You may exceed the allocation eventually and need to move anyway.

## Linked Lists

Items can be anywhere in memory, and each items stores the address
of the next item in the list. A bunch of random memory addresses
are linked together. Adding an item is easy- store it anywhere and
tack on that new address to the previous item. 
Each element in a linked list is called a node, and they store the data
and the address of the next node.
You never have to move your items.

## Arrays vs Linked Lists - Use Cases

**Run times for common operations on arrays and linked lists**  
| operation | arrays | LLs |
|-----------|--------|-----|
|Reading    | O(1)   |O(n) |
|Insertion  | O(n)   |O(1) |
|Deletion   | O(n)   |O(1) | 

One problem with linked lists concerns navigation. The only way to 
find a particular items is to run thru everything in the linked list
that preceeds it.  
Linked lists are great if you know you're gonna read all the items 
one at a time. But if you're gonna jump around, they're terrible.  
  
With arrays, you know the address for every item in your array. They
are great if you want to read random elements.  
  
If you need to add items at various places within your structure,
with linked lists, all you need to do is chance where the previous
element points to. With arrays, however, you need to shift everything
down to make space in the middle, and also possibly have to move 
the entire thing.   
  
If you're going to be deleting stuff a lot, again, linked lists are
better because you just have to adjust what a previous element points
to.  

**Random Access vs Sequential Access**  
Linked lists can only do sequential, which is what it sounds like.
Arrays can do both, with random access being availability to jump
to any element. Arrays are generally faster at reads because of 
random access ability.
