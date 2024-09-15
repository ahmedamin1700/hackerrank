
def main():
    # n = int(input())
    t = tuple(map(int, input().split()))

    hash_tuple = hash(t)
    print(hash_tuple)


if __name__ == '__main__':
    main()
