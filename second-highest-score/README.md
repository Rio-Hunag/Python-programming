# Second Highest Score

## Overview

A Python program that finds the second-highest distinct score from a list of integers.

## Features

- Accepts a list of numerical scores.
- Removes duplicate values.
- Sorts the distinct scores in descending order.
- Returns the second-highest distinct score.

## Approach

1. Read the number of scores and the score values.
2. Convert the scores into a set to remove duplicates.
3. Sort the distinct scores in descending order.
4. Select the second element from the sorted list.
5. Print the result.

## Example

**Input**
```text
5
2 3 6 6 5
```

**Output**
```text
5
```

## Complexity

Let `n` be the number of scores.

- **Time Complexity:** O(n log n), due to sorting.
- **Space Complexity:** O(n), for storing the distinct scores.

## Language

Python

## Files

- `main.py` — program implementation.
- `README.md` — project documentation.
