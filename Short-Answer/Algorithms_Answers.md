#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) This function sets the value of a to (n squared) while (n cubed) is greater than a, so it's time complexity would be O(n).


b) O(n²) This function is O(n²) because it contains a loop nested inside of another loop, each individually would be O(n), but when nesting we're actually running one entire loop through n for every iteration of the parent loop, giving us an exponential time increase as n grows.


c) O(n) This funtion is called recursively n amount of times until it reaches it's
base case. We are not doing anything complex with the recursion, simply addinng 2 for ears for each bunny which gives us O(n2), or simplified O(n).  
## Exercise II

My proposed solution to the egg drop problem is to use a binary search to find the ideal egg drop height.

First we would need set a base case, for `0` floors or `0` eggs, we can not preform the drop. We could use a while loop to continue running the code until either is reached.
Next we should initialize the values of the floors, `n` being the maximum value and `1` being the minimum. 
After that we should compare the values of `min` and `max` as the value of each has the potential to change as we continue, so as long as the `min < max` 
We could then find the median by adding the max and min values and dividing by `2` and set this value to `mid`. 
Presumably then we would need some sort of function to evaluate whether the egg was broken or not, though I can't imagine an egg drop from even the first floor would be successful. Upon a failed drop we should change the `min` value to the `mid + 1` and evaluate the lower floors, or upon a successful drop, `max` should be made the new `mid` to evaluate the higher floors until the lowest success value is reached, in this case when `min` and `max` are equivalent. 

I believe the implementation of this algorithm would result in a O(n log(n)) time value, since the operation is performing `log(n)` operations for every occurence of `n`; every range of levels divided until the correct level is reached.
