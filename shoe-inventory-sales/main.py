
from collections import Counter


def calculate_sales(shoe_sizes, customers):
    inventory = Counter(shoe_sizes)
    total_earned = 0

    for size, price in customers:
        if inventory[size] > 0:
            total_earned += price
            inventory[size] -= 1

    return total_earned


def main():
    num_shoes = int(input())
    shoe_sizes = list(map(int, input().split()))

    num_customers = int(input())
    customers = []

    for _ in range(num_customers):
        size, price = map(int, input().split())
        customers.append((size, price))

    total_earned = calculate_sales(shoe_sizes, customers)
    print(total_earned)


if __name__ == "__main__":
    main()
