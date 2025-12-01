# main.py (merged with compute logic)
# Contains compute logic and CLI in one file.

from willans_detectors import wilsons_detector, trial_division_detector


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


if __name__ == "__main__":
    import sys

    try:
        n = int(input("Enter n: "))
        method = input("Method ('wilson' or 'trial'): ").strip().lower()
    except Exception:
        print("Invalid input.")
        sys.exit(1)

    primes, nth = compute_primes_up_to_n(n, method)

    print("Primes up to n:")
    print(primes)
    print(f"Final: {n}th prime = {nth}")