# Unique Set Values

## Overview

A Python program that identifies values appearing in exactly one of two sets of integers.

## Features

- Reads two sets of integers.
- Finds values that appear in one set but not both.
- Removes duplicate values through set operations.
- Sorts the results in ascending order.

## Approach

1. Read the integer values for both sets.
2. Convert the values into Python sets.
3. Calculate the symmetric difference between the sets.
4. Sort the resulting values.
5. Print each value on a separate line.

## Example

**Input**
```text
4
2 4 5 9
4
2 4 11 12
```

**Output**
```text
5
9
11
12
```

## Complexity

Let `m` and `n` be the numbers of elements in the two sets.

- **Expected Time Complexity:** O(m + n) for set operations, plus O(k log k) for sorting the `k` resulting values.
- **Space Complexity:** O(m + n) for storing the sets and result.

## Language

Python

## Files

- `main.py` — program implementation.
- `README.md` — project documentation.
