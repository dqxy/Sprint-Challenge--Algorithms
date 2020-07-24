#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) - performance will grow linearly and in direct proportion to the size of the input data set.  After each iteration the value of 'a' increases by (n * n) plus the previous value of a. n * n is canceleld out for O(n).


b) O(n log n) Outer for loop runs linearly. In the inner while loop, increasing the value of j by the previous value multiplied by 2 makes the inner loop run time logn as it increases at a higher rate. In the inner level the size of array is reduced by half 


c) O(n) Even though function is recursively called, it is still linearly calculated.  Increasing the number of bunnies will increase the amount of work to be done by same amount

## Exercise II

A Binary Search algorithm should be used. Beginning on the middle floor, drop the egg - if it breaks then calculate the scope of floors to be tested from that floor and below, then repeat the calculation until the egg stays intact. This will result in the least number of broken eggs and bring about our solution.

Runtime will be O(log n) because the range of possible solutions is cut in half for each loop iteration.