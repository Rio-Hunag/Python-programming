if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    unique_score=set(arr)
    sorted_score=sorted(unique_score)
    print(sorted_score[-2])
