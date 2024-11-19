#reference/publication

[[000 - Reading List]]

- what this paper does
	- Generalises mutliplexed sensing and analyses advantages

- What is multiplexing
	- [[PHYS3051L42 Multiplexing]] [[PHYS3051T10 Multiplexing]] and [[PHYS3051 Exam Preparation]]
		- All of these notes touch on multiplexing
	- Measuring many points in space/time/energy and using DSP (?) to separate each measurement
	- By taking many multiplexed measurements you can decode same information as a systematic scan over the same range of depth etc
	- Multiplexing can be advantageous in some scenarios, mostly in engineering design of the instrumentation

- Paper's outcomes are that
	- Multiplexing allows "post production" variation of resolution
	- Multiplexing can overcome specific types of noise (Felgett's advantage), but doesn't actually capture more information
		- Rastering is always best when reducing noise ratio
	- If the sample is sparse and you can do compressive sensing, there is significant advantage to using multiplexed sensing due to reductions in experiment time, radiation does etc

- Framework
	- We take $m$ different samples of $n$ channels (which can be some total sum of pixels)
	- each channel may have $k$ different outputs (i.e. different coloured pixels)
	- $R = m \times k$ is the total number of recorded outcomes per channel
	- $A = m \times n$ is the sensing matrix
		- Clarify what a sensing matrix is
		- note if $m=n$ this is the same as just imaging each pixel individually
	- $X =n \times k$ is the output signal of interest that we want to reconstruct
	- $\epsilon$ is a $m\times k$ random noise matrix
	- thus the output will be $R=AX+\epsilon$
	- Thus if we know $A$ and we can guess different combos for $X$, we can find an estimated output of $\hat{X}$ as:
	$$
\hat{X}=argmin||R-AX||^2
$$
- The optimal solution can be proven to be a ordinary least square solution, and the paper has proofs for this & the exact error in the appendix
- Paper then goes into breakdown of noise contributions




![[What are the advantages of ghost imaging_ Multiplexing for x-ray and electron imaging - oe-28-5-5898.pdf]]