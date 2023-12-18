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

![Graph showing difference in runtime](/imgs/rec_vs_iterative.png)
## Can we do better?

The iterative technique is much better than the recursive technique, but it still has time complexity of n.

![Graph showing scaling of higher values of n](/imgs/iterative_vs_bestfit.png)

If we could find a technique with log(n) or even 1 complexity, this would vastly outpace our iterative technique at higher values of the fibonacci sequence.
## Matrices, Diagonalisation, and Closed Form Solutions
### Matrices as Linear Transformations
A matrix can be used to represent any linear transformation. For the fibonacci sequence, if we define our Matrix M as

![equation](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D%5Cbg%7Bwhite%7DM=%5Cbegin%7Bpmatrix%7D0&1%5C%5C1&1%5C%5C%5Cend%7Bpmatrix%7D)

Then, 

![equation](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D%5Cbg%7Bwhite%7D%5Cleft(%5Cbegin%7Barray%7D%7Bcc%7D0&1%5C%5C1&1%5Cend%7Barray%7D%5Cright)%5Cleft(%5Cbegin%7Barray%7D%7Bcc%7Dx_n%5C%5Cx_%7Bn&plus;1%7D%5Cend%7Barray%7D%5Cright)=%5Cleft(%5Cbegin%7Barray%7D%7Bcc%7Dx_%7Bn&plus;1%7D%5C%5Cx_%7Bn&plus;2%7D%5Cend%7Barray%7D%5Cright))

This is true because, if you perform the matrix vector multiplication, the equation simplifies to:

![equation](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D%5Cbg%7Bwhite%7D%5Cleft(%5Cbegin%7Barray%7D%7Bcc%7D0*x_n&plus;1*x_%7Bn&plus;1%7D%5C%5C1*x_n&plus;1*x_%7Bn&plus;1%7D%5Cend%7Barray%7D%5Cright)=%5Cleft(%5Cbegin%7Barray%7D%7Bcc%7Dx_%7Bn&plus;1%7D%5C%5Cx_%7Bn&plus;2%7D%5Cend%7Barray%7D%5Cright))

Which follows the formula for the fibonacci sequence.
We can test this for a few values of n.

![equation](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D%5Cbg%7Bwhite%7Dx_0=0,x_1=1,x_2=1,x_3=2,x_4=3,x_5=5)

![equation](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D%5Cbg%7Bwhite%7D%5Cleft(%5Cbegin%7Barray%7D%7Bcc%7D0&1%5C%5C1&1%5Cend%7Barray%7D%5Cright)%5Cleft(%5Cbegin%7Barray%7D%7Bcc%7Dx_0%5C%5Cx_%7B1%7D%5Cend%7Barray%7D%5Cright)=%5Cleft(%5Cbegin%7Barray%7D%7Bcc%7D0&plus;1%5C%5C0&plus;1%5Cend%7Barray%7D%5Cright)=%5Cleft(%5Cbegin%7Barray%7D%7Bcc%7D1(x_%7B1%7D)%5C%5C1(x_%7B2%7D)%5Cend%7Barray%7D%5Cright))

![equation](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D%5Cbg%7Bwhite%7D%5Cleft(%5Cbegin%7Barray%7D%7Bcc%7D0&1%5C%5C1&1%5Cend%7Barray%7D%5Cright)%5Cleft(%5Cbegin%7Barray%7D%7Bcc%7Dx_1%5C%5Cx_2%5Cend%7Barray%7D%5Cright)=%5Cleft(%5Cbegin%7Barray%7D%7Bcc%7D0&plus;1%5C%5C1&plus;1%5Cend%7Barray%7D%5Cright)=%5Cleft(%5Cbegin%7Barray%7D%7Bcc%7D1(x_%7B2%7D)%5C%5C2(x_%7B3%7D)%5Cend%7Barray%7D%5Cright))

![equation](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D%5Cbg%7Bwhite%7D%5Cleft(%5Cbegin%7Barray%7D%7Bcc%7D0&1%5C%5C1&1%5Cend%7Barray%7D%5Cright)%5Cleft(%5Cbegin%7Barray%7D%7Bcc%7Dx_2%5C%5Cx_3%5Cend%7Barray%7D%5Cright)=%5Cleft(%5Cbegin%7Barray%7D%7Bcc%7D0&plus;2%5C%5C1&plus;2%5Cend%7Barray%7D%5Cright)=%5Cleft(%5Cbegin%7Barray%7D%7Bcc%7D2(x_%7B3%7D)%5C%5C3(x_%7B4%7D)%5Cend%7Barray%7D%5Cright))

![equation](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D%5Cbg%7Bwhite%7D%5Cleft(%5Cbegin%7Barray%7D%7Bcc%7D0&1%5C%5C1&1%5Cend%7Barray%7D%5Cright)%5Cleft(%5Cbegin%7Barray%7D%7Bcc%7Dx_3%5C%5Cx_4%5Cend%7Barray%7D%5Cright)=%5Cleft(%5Cbegin%7Barray%7D%7Bcc%7D0&plus;3%5C%5C2&plus;3%5Cend%7Barray%7D%5Cright)=%5Cleft(%5Cbegin%7Barray%7D%7Bcc%7D3(x_%7B4%7D)%5C%5C5(x_%7B5%7D)%5Cend%7Barray%7D%5Cright))
### Powers of Matrices
Using proof by mathematical induction, we can prove

![equation](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D%5Cbg%7Bwhite%7DM%5Ek%5Cleft(%5Cbegin%7Barray%7D%7Bcc%7Dx_0%5C%5Cx_1%5Cend%7Barray%7D%5Cright)=%5Cleft(%5Cbegin%7Barray%7D%7Bcc%7Dx_k%5C%5Cx_%7Bk&plus;1%7D%5Cend%7Barray%7D%5Cright))

For the base case:

![equation](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D%5Cbg%7Bwhite%7D%20M%5E1%5Cleft(%5Cbegin%7Barray%7D%7Bcc%7Dx_0%5C%5Cx_1%5Cend%7Barray%7D%5Cright)=M%5Cleft(%5Cbegin%7Barray%7D%7Bcc%7Dx_0%5C%5Cx_1%5Cend%7Barray%7D%5Cright)=%5Cleft(%5Cbegin%7Barray%7D%7Bcc%7Dx_1%5C%5Cx_2%5Cend%7Barray%7D%5Cright))

![equation](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D%5Cbg%7Bwhite%7DM%5E2%5Cleft(%5Cbegin%7Barray%7D%7Bcc%7Dx_0%5C%5Cx_1%5Cend%7Barray%7D%5Cright)=MM%5Cleft(%5Cbegin%7Barray%7D%7Bcc%7Dx_0%5C%5Cx_1%5Cend%7Barray%7D%5Cright)=M%5Cleft(%5Cbegin%7Barray%7D%7Bcc%7Dx_1%5C%5Cx_2%5Cend%7Barray%7D%5Cright)=%5Cleft(%5Cbegin%7Barray%7D%7Bcc%7Dx_2%5C%5Cx_3%5Cend%7Barray%7D%5Cright))

For the recusive step:
- We must assume that our formula is true for M<sup>k</sup>, and prove it for M<sup>k+1</sup>

![equation](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D%5Cbg%7Bwhite%7DM%5E%7Bk&plus;1%7D%5Cleft(%5Cbegin%7Barray%7D%7Bcc%7Dx_0%5C%5Cx_1%5Cend%7Barray%7D%5Cright)=MM%5Ek%5Cleft(%5Cbegin%7Barray%7D%7Bcc%7Dx_0%5C%5Cx_1%5Cend%7Barray%7D%5Cright)=M%5Cleft(%5Cbegin%7Barray%7D%7Bcc%7Dx_k%5C%5Cx_%7Bk&plus;1%7D%5Cend%7Barray%7D%5Cright)=%5Cleft(%5Cbegin%7Barray%7D%7Bcc%7Dx_%7Bk&plus;1%7D%5C%5Cx_%7Bk&plus;2%7D%5Cend%7Barray%7D%5Cright))

Because we have proven the formula for the base case k=2 and for the recursive case, the formula is proven by mathematical induction.

### Diagonalisation and the Closed Form
Using Matrix Properties, the formula for the k<sup>th</sup> power of a Matrix can be expressed as with a closed form equation using diagonalisation. 

![equation](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D%5Cbg%7Bwhite%7DM%5Ek=PD%5EkP%5E%7B-1%7D)

D<sup>k</sup> is a closed form matrix as it is a diagonal matrix.
P is the matrix formed from eigenvectors of M, and D is the matrix formed from placing the eigenvalues along the diagonal and 0's on all other spaces.

Using the numpy module's matrix and linear algebra libraries, we can provide a function to find 

![equation](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D%5Cbg%7Bwhite%7DM%5Ek=PD%5EkP%5E%7B-1%7D)

## Closed Form Function
Using the numpy library, I created the following function to calculate the x<sub>index</sub> value of the Fibonacci sequence
~~~
def closed_form(index):
    M = np.mat(np.array([[0,1],[1,1]]))
    #Creates matrix for M
    eigvals, P = np.linalg.eig(M)
    #Stores eigen vectors in P
    D = np.mat(np.array([[eigvals[0]**index, 0], [0, eigvals[1]**index]]))
    #Transforms eigen values to form necessitated by D
    Pinv = np.linalg.inv(P)
    #Store P inverse
    PDPinv = np.matmul(np.matmul(P, D), Pinv)
    #Gets PD^kP^-1
    return PDPinv[0, 1]
    #Because x0 = 0 and x1 = 1, matrix-vector multiplication would return the element in row 0, column 1
~~~

### Runtime
This function will doesn't scale with N, meaning that it has a constant runtime 

$\theta$(F(n)) = $\theta$(1)

### Trade Off
This solution is the most efficient way to find values in the fibonacci sequence. However, it suffers from inaccuracy due to the fundamental inaccuracies of floating point arithmetic in computers. Therefore, it won't specify the exact value, but a value extremely close to the correct value.
This inaccuracy will become worse for higher values of the sequence, as they require more arithmetic.

## Runtime Comparison

![image](/imgs/iter_vs_closed.png)
