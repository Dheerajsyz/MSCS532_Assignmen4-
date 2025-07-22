# Quicksort Assignment

## Implementation

All code is in `quicksort_assignment.py`, which contains:
- Deterministic Quicksort (last element as pivot)
- Randomized Quicksort (random pivot)
- Empirical analysis comparing both algorithms

## Performance Analysis

**Time Complexity:**
- Best Case: O(n log n) — Pivot splits array evenly
- Average Case: O(n log n) — Random/well-distributed pivots
- Worst Case: O(n²) — Pivot always smallest/largest (e.g., sorted input for deterministic)

**Why Average Case is O(n log n):**
On average, partitioning produces balanced subarrays, leading to log n recursion levels, each processing n elements.

**Space Complexity:**
- In-place: O(log n) stack space (best/average), O(n) (worst)

## Randomized Quicksort

Randomization chooses a random pivot, making worst-case splits rare and improving robustness, especially for adversarial or sorted data.

## Empirical Analysis

Run:
```
python quicksort_assignment.py
```
This prints timing results for both algorithms on random, sorted, and reverse-sorted arrays of various sizes.

<img width="1234" height="494" alt="CleanShot 2025-07-22 at 18 47 08@2x" src="https://github.com/user-attachments/assets/e34dacce-56e4-4380-befd-6685bba75e15" />


