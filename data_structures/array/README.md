# Linear Data Structure - Array

An **array** is a fundamental linear data structure that stores a collection of elements of the same data type in contiguous (adjacent) memory locations. Each item in an array is an element, and its position is uniquely identified by a numerical *index*, which typically starts at 0.


## Time Complexity of Operations

| Operation         | Time Complexity        |
|-------------------|------------------------|
| Access/Read       | O(1) - Constant        |
| Update            | O(1) - Constant        |
| Insertion         | O(n) - Linear          |
| Deletion          | O(n) - Linear          |
| Search (unsorted) | O(n) - Linear          |
| Search (sorted)   | O(log n) - Logarithmic |


## Static Arrays vs. Dynamic Arrays


### Static Arrays

A **static array** is a fundamental data structure defined as a contiguous block of memory with a fixed size determiend at compile time. Once you declare a static array, its capacity cannot be altered, meaning you cannot expand or shrink its structure during the execution of your program.


### Dynamic Arrays

A **dynamic array** is a random-access, variable-size list data structure that automatically expands its capacity when it runs out of space. Unlike static arrays, which require a fixed capacity at compile time, dynamic arrays allocate memory at runtime to accommodate new elements seemlessly.