# Shoe Inventory Sales

## Overview

A Python program that calculates total sales revenue based on available shoe sizes and customer purchase requests.

## Features

- Tracks available inventory for each shoe size.
- Processes customer requests in order.
- Accepts a purchase only when the requested size is in stock.
- Updates inventory after each successful sale.
- Calculates the total revenue earned.

## Approach

1. Count the available shoes of each size using `Counter`.
2. Read each customer's requested size and offered price.
3. Check whether the requested size is available.
4. If available, add the price to the total revenue and reduce the inventory count by one.
5. Output the total revenue after processing all customers.

## Example

**Input**
```text
10
2 3 4 5 6 8 7 6 5 18
6
6
6 55
6 45
6 55
4 40
18 60
10 50
```

**Output**
```text
200
```

## Complexity

Let `n` be the number of shoes and `m` be the number of customer requests.

- **Expected Time Complexity:** O(n + m)
- **Space Complexity:** O(n + m), including inventory and stored customer requests.

## Language

Python

## Files

- `main.py` — program implementation.
- `README.md` — project documentation.
