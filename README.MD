# Willans Prime Generator

A Python implementation of Willans' formula for computing the **nth prime number**, using two interchangeable primality detectors:

- **Wilson-based detector** (theoretically elegant, extremely slow)
- **Trial-division detector** (practically faster, simpler)

The project provides:

- Modular detector implementations
- A unified compute system
- A benchmarking script
- Graph output comparing detector efficiency
- A CLI for generating primes and printing all primes ≤ n

---

##  Project Structure

```
/project
│
├── detectors.py              # Wilson + Trial primality detectors
├── willans.py                # Main Willans compute module
├── main.py                   # CLI runner (merged logic)
├── compare_detectors.py      # Benchmark + PNG plot
└── README.md                 # This file
```

---

# 1.  Mathematical Background

Willans' formula (1949) gives an exact closed-form expression for the nth prime:

\[
p_n = 1 + \sum_{i=1}^{2^n}
\left\lfloor  
    \left( \frac{n}{1 + \pi(i)} \right)^{1/n}  
\right\rfloor
\]

Where:
- \(\pi(i)\) is the prime-counting function
- The term becomes **1** if \(\pi(i) < n\) and **0** otherwise

To compute this, we need a **function that can tell whether i is prime or not**.
This is where the primality detectors come in.

---

# 2.  Trial Division Detector

## 2.1 Mathematical Theorem

Trial division is based on a fundamental property:

> **A composite number must have a factor ≤ √n.**

Equivalently:

\[
n \text{ is prime } \iff n > 1 \text{ and no integer } d \in [2,\sqrt{n}] \text{ divides } n.
\]

This follows from the fact that if:
\[
n = a \cdot b
\]
then at least one of \(a, b\) is ≤ √n.

---

## 2.2 Trial Division Detector Function

```python
def trial_division_detector(j: int) -> int:
    if j <= 1:
        return 0
    if j == 2:
        return 1
    if j % 2 == 0:
        return 0

    limit = int(math.isqrt(j))
    for k in range(3, limit + 1, 2):
        if j % k == 0:
            return 0
    return 1
```

- Returns **1** if j is prime
- Returns **0** if j is composite

This satisfies the Willans requirement for a primality indicator.

---

# 3.  Wilson's Theorem Detector

## 3.1 Mathematical Theorem Behind It

Wilson's theorem states:

\[
p \text{ prime } \iff (p - 1)! \equiv -1 \mod p.
\]

Meaning:
- For primes, `(p−1)! + 1` is divisible by p
- For composites, it is never true

This allows the prime indicator:

\[
W(j) = 1 \text{ if } (j - 1)! \equiv -1 \mod j \text{ else } 0
\]

---

## 3.2 Wilson Detector Function

```python
def wilsons_detector(j: int) -> int:
    if j <= 1:
        return 1

    fact_mod = 1
    for k in range(1, j):
        fact_mod = (fact_mod * k) % j
        if fact_mod == 0:
            return 0

    numerator = (fact_mod + 1) % j
    val = (numerator / j) * math.pi
    return math.floor((math.cos(val)) ** 2)
```

Note: The cosine expression is mathematically valid because we only care about the value modulo \(j\), and the cosine collapses to 1 exactly when `(fact_mod + 1) % j == 0`.

---

# 4.  Willans Compute Function

The shared compute function determines the nth prime using either detector.

```python
def compute_primes_up_to_n(n: int, method: str = "wilson"):
    if method == "wilson":
        detector = wilsons_detector
    elif method == "trial":
        detector = trial_division_detector
    else:
        raise ValueError("method must be 'wilson' or 'trial'")

    detector_cache = {}
    pi_cache = {}
    primes = []
    M = 2 ** n

    for i in range(1, M + 1):
        if i not in detector_cache:
            detector_cache[i] = detector(i)

        pi_cache[i] = pi_cache.get(i - 1, 0) + detector_cache[i]
        pi_i = pi_cache[i]

        if detector_cache[i] == 1:
            primes.append(i)

        if pi_i == n:
            return primes, i

    raise RuntimeError("Upper bound failed. Increase M.")
```

### Output
- A list of primes ≤ n
- The nth prime

---

# 5.  Benchmarking & Plotting

The script `compare_detectors.py` compares runtimes:
- Wilson detector vs trial division
- Plots time vs n
- Saves output as a PNG

### Run benchmark
```
python compare_detectors.py
```

Produces:
- `detector_comparison.png`

---

# 6.  CLI Usage

```
python main.py
```
Output example:
```
Enter n: 10
Method ('wilson' or 'trial'): trial
Primes up to n:
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
Final: 10th prime = 29
```

---

# 7.  Performance Notes

- **Trial division** is *much* faster than Wilson-based detection.
- Wilson-based method is mostly mathematical interest.
- Willans’ formula is extremely slow for large n regardless of detector.

---

# 8. 📚 References
- Willans, C. "On Formulae for the nth Prime Number." *The American Mathematical Monthly*, 1949.
- Wilson, J. Theorem relating factorials and prime numbers.
- Basic Number Theory — Trial Division and Primality Testing.

---

#  End
This README documents the theoretical basis, implementation details, and usage of the Willans prime generator project.

Feel free to expand with more detectors, optimizations, or visualizations!
