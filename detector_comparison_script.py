# compare_detectors.py
# Compares Wilson-based detector vs Trial Division detector.
# Produces a graph: x = n, y = time to compute nth prime.

import time
import matplotlib.pyplot as plt
from willans import compute_primes_up_to_n

# compute_primes_up_to_n already handles nth prime detection


def benchmark(method, max_n):
    times = []
    for n in range(1, max_n + 1):
        start = time.time()
        compute_primes_up_to_n(n, method)
        end = time.time()
        times.append(end - start)
    return times


def main():
    max_n = int(input("Benchmark up to n = "))

    print("Running Wilson detector benchmark...")
    wilson_times = benchmark("wilson", max_n)

    print("Running Trial Division benchmark...")
    trial_times = benchmark("trial", max_n)

    # Plot results
    x = list(range(1, max_n + 1))
    plt.plot(x, wilson_times, label="Wilson Detector")
    plt.plot(x, trial_times, label="Trial Division Detector")

    plt.xlabel("n (nth prime)")
    plt.ylabel("Time (seconds)")
    plt.title("Detector Speed Comparison")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    
    # Save before showing (some backends clear the figure on show)
    plt.savefig("detector_comparison.png", dpi=200, bbox_inches='tight')
    print(f"Plot saved as 'detector_comparison.png'")
    plt.show()


if __name__ == "__main__":
    main()
