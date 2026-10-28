
def find_second_highest(scores):
    unique_scores = sorted(set(scores), reverse=True)

    if len(unique_scores) < 2:
        raise ValueError("At least two distinct scores are required.")

    return unique_scores[1]


def main():
    n = int(input())
    scores = list(map(int, input().split()))

    if n != len(scores):
        raise ValueError("The number of scores does not match the input.")

    print(find_second_highest(scores))


if __name__ == "__main__":
    main()
