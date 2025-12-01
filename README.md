Willans Prime Generator
-----------------------

This project implements a computational version of Willans’ formula for determining the nth prime number.Instead of evaluating the symbolic closed form directly, the method rebuilds Willans’ prime-indexing logic using:

• A primality detector• A running prime counter• A termination condition when the nth prime is reached

Two detectors are implemented:

1.  Trial Division Detector — recommended, fast, deterministic
    
2.  Wilson’s Theorem Detector — mathematically elegant but much slower
    

A benchmarking script compares both detectors and produces a timing graph.

1.  Mathematical Background
    

Willans’ conceptual prime-index form is:

p\_n = 1 + ∑ from m=1 to 2^n of 1{ 1 + ∑ from j=1 to m P(j) ≤ n }

Here:

• P(j) is 1 if j is prime and 0 otherwise• The inner sum counts primes less than or equal to m• The indicator stays 1 while the count is less than n• It becomes 0 as soon as the nth prime is reached

Thus p\_n is the smallest m for which π(m) = n.

1.  Trial Division Primality Detector
    

Mathematical Basis:

A number n is prime if and only if n > 1 and no integer d in the interval \[2, √n\] divides n.This comes from the fact that if n = ab, then at least one of a or b must be ≤ √n.

Detector Definition:

T(n) returns 1 if:

• n = 2; or• n is odd and has no divisor up to √n

Otherwise, it returns 0.

This detector is:

• deterministic• exact for all integers• very efficient for all practical values

Why Trial Division Is Faster:

Wilson’s theorem requires computing (n − 1)! mod n, which takes O(n) modular multiplications.Trial division requires at most O(√n) lightweight integer checks.In practice:

• even numbers are rejected immediately• most composites have small factors• only primes require checking up to √n

As a result, trial division is more than an order of magnitude faster than Wilson’s method.

1.  Wilson’s Theorem Detector (Reference Only)
    

Wilson’s theorem states:

n is prime if and only if (n − 1)! ≡ −1 (mod n).

This produces a correct primality test but is extremely slow because factorial growth is rapid.Even with modular reduction, evaluating (n − 1)! mod n is expensive.This detector is included for completeness, not performance.

1.  Modified Willans Prime Computer
    

The prime generator uses:

π(m) = number of primes ≤ m

and computes:

p\_n = ∑ from m=1 to B(n) of 1{ 1 + π(m) ≤ n }

It stops exactly when π(m) = n.

B(n) is a safe upper bound on the nth prime.The classical Willans bound (2^n) is kept for structural fidelity, but other bounds can be substituted when using fast detectors.

1.  Benchmark Summary
    

The benchmark compares the trial division detector and the Wilson detector by measuring the time required to compute successive values of n.

The plotted graph (detector\_comparison.png) shows:

• The trial division curve grows slowly and steadily.• The Wilson curve grows rapidly with noticeable spikes due to the cost of modular factorial computation.• For every tested value, trial division is dramatically faster.

1.  Summary
    

• Willans’ structure is mathematically elegant for locating prime indices.• The primality detector P(j) largely determines performance.• Trial division is simple, deterministic, and significantly faster than Wilson’s theorem.• The modified Willans prime computer implemented in this project is efficient for moderate n and demonstrates the practical difference between detectors.