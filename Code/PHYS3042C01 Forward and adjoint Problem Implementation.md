#worked 
**18/11/24**

## Questions
 - What is the reasoning behind $A^T(b-\left<b\right>) \approx 0$ being a reasonable approximation? The output does not look even close! 
 - How should I deal with compute time? My laptop was struggling to run simulations for $m>100$..
 - 
## Explanation

We're trying to implement
$$
Ax=b
$$
Where $x$ is the flattened array representation of a signal (in this case our image), $A$ is a array of $m$ different masks, each mask is the length of the image, and $b$, which are our bucket values, representing an $m$ array of the cross product of the image with each of the $m$ different masks.

We first have to generate the mask $A$ - I wrote two functions to either do this with a binary mask, or with a gaussian mask. I'm not sure what a Gaussian mask would look like in real life...

The forward ghost functions accept an image, the desired number of bucket values, and some mask generation function (so I could swap between the binary/gauss masks), and generates the array of bucket values by calculating $Ax=b$. The matrix function just presents the matrix based approach 

The inverse functions calculate an approximation for $x$ by taking $A^pb$ (where $A^p$ is *(my choice of notation for)* the Moore–Penrose inverse (pinv func), which is a pseudo inverse matrix). The other approach is by calculating $x\approx A^T(b-\left<b\right>)$. Both of these inverse functions then reshape the array into the desired 2d form.


I do find it a bit difficult to always be thinking interms of matrix/vector shape. I need to refresh my intuition for vector/matrix operations because I keep confusing myself..

Input:
![[PHYS3042C01 Fig1.png]]
Output:
![[PHYS3042C01 Fig2.png]]
## Code
```embed-python
PATH: "vault://Courses/PHYS3042/Code/Source/Ghost Imaging Helper Functions.py"
```


## Brief
*To describe the forward and adjoint problems:*
 *forward problem is Ax = b where*
*"x" is the image written in vectorised form, e.g., a 3 x 3 pixel image:*
*[ 1 2 3 ]*
*[ 4 5 6 ]*
*[ 7 8 9 ]*

*would become:*
*[ 1 2 3 4 5 6 7 8 9  ] ^T (where T is "transpose")*
*"A" is the set of patterns. Each pattern is written in a row (the same as the image above but without the transpose), so M patterns will give you M rows of the matrix. If the image has N pixels, then A is an M x N matrix. something to investigate is how things change as M is <<N, <N, =N, >N, >>N. "b" is the set of "bucket values" associated with each mask.*
*You can calculate Ax = b either by writing everything in matrix form as described above, or by just doing image processing, e.g., the "j"th bucket value is the dot product of mask "j" with the image:*  
*b[j] = A[j].x*
*OR you may find another better/faster way to calculate it.*  

adjoint problem is $x'$ = A^T(b-<b>) where x' is an approximation of the original "x" and <b> is the mean bucket value (that is subtracted from all bucket values).
*this can again be implemented as matrices (if you have done it as matrices, you could also try x' = A_inv b where A_inv is the Moore-Penrose inverse)
*the image processing version is that x' is the sum of all patterns weighted by the bucket value - <b>, i.e.,*
*x' += A[j] * (b[j] - <b>) over all j in [0..M-1]*  
*OR again you may find your own way to do this.*  

