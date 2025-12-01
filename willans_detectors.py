# detectors.py
# Contains both Wilson-based and Trial Division-based primality detectors.

import math

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
