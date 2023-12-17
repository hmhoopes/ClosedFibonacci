# Fibonacci Sequence
## Recusive Function
Our recursive function for finding the n<sup>th</sup> element of the fibonacci sequence is relatively simple.
- If n is 0, return 0
- If n is 1, return 1
- Else, return the value of n-1 element plus the value of the n-2 element.
~~~
def rec_finder(index):
    if index == 0:
        return 0
    elif index == 1:
        return 1
    return rec_finder(index - 1) + rec_finder(index - 2)
~~~
### Runtime
Let's designate F(n) as a representation of calling rec_finder(n).
The call F(n) requires F(n-1)+F(n-2) steps. 
- F(n) = F(n-1) + F(n-2)
 
For F(n-1), it will require F(n-2)+F(n-3) steps
For F(n-2), it will require F(n-3)+F(n-4) steps 
- F(n) = F(n-2)+F(n-3)+F(n-3)+F(n-4)
- F(n) = F(n-4)+F(n-5)+F(n-4)+F(n-5)+F(n-4)+F(n-5)+F(n-5)+F(n-6)

Notice that, at each level on of calls, we are calling twice as many as the level above.
- F(n-1)+F(n-2) -> 2 calls
- F(n-2)+F(n-3)+F(n-3)+F(n-4) -> 4(2 * 2) calls
- F(n-4)+F(n-5)+F(n-4)+F(n-5)+F(n-4)+F(n-5)+F(n-5)+F(n-6) -> 8(2 * 2 * 2) calls

The number of calls, if we express the current level as L, is 2<sup>L</sup>

How many levels do we go down? To answer this, let us consider F(n) once more.
- F(n) = F(n-1)+F(n-2)

To solve this, we must solve F(n-1)
- F(n-1) = F(n-2)+F(n-3)
To solve this, we must solve F(n-2)

This pattern will continue until we reach F(2), where F(2) = F(1)+F(0)

So, in order to resolve F(n), we must call F(n), F(n-1), ... , F(1)

So, we traverse n-1 levels.

Then, we can express the steps performed as 2<sup>1</sup>+2<sup>2</sup>+...+2<sup>n-1</sup>

By the rules for Big-$\theta$ notation, the runtime of this function is:

 $\theta$(F(n)) = $\theta$(2<sup>n</sup>)

## Iterative Function
Our iterative function for finding the n<sup>th</sup> element of the fibonacci sequence requires iterating n times.
~~~
def iterative_finder(index):
    if index == 0:
        return 0
    first = 1
    second = 0
    for i in range(1, index):
        temp = first
        first += second
        second = temp
    return first
~~~
### Runtime
Thankfully, calculating the runtime for this algorithm is much simpler. For index n, we must perform n-2 iterations.

Therefore, if we have F(n) representing our iterative function, $\theta$(F(n)) = $\theta$(n)
## Comparison Graph
The following graph illustrates the incredible jump in time efficiency when changing from a recursive to an iterative technique.

![Graph showing difference in runtime](/rec_vs_iterative.png)
## Can we do better?

The iterative technique is much better than the recursive technique, but it still has time complexity of n.

![Graph showing scaling of higher values of n](/iterative_vs_bestfit.png)

If we could find a technique with log(n) or even 1 complexity, this would vastly outpace our iterative technique at higher values of the fibonacci sequence.
## Closed Form Equation