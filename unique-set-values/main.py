
def find_unique_values(first_set, second_set):
    return sorted(first_set.symmetric_difference(second_set))


def main():
    first_count = int(input())
    first_set = set(map(int, input().split()))

    second_count = int(input())
    second_set = set(map(int, input().split()))

    result = find_unique_values(first_set, second_set)

    for number in result:
        print(number)


if __name__ == "__main__":
    main()
