
def main():
    result_list = []
    # n = int(input())

    file = open('sample_input_1(N=29).txt', 'r')
    lines = file.readlines()

    # for i in range(n):
    for line in lines:
        request = line.split()
        if request[0] == 'insert':
            result_list.insert(int(request[1]), int(request[2]))
        if request[0] == 'remove':
            result_list.remove(int(request[1]))
        if request[0] == 'append':
            result_list.append(int(request[1]))
        if request[0] == 'sort':
            result_list.sort()
        if request[0] == 'pop':
            result_list.pop()
        if request[0] == 'reverse':
            result_list.reverse()
        if request[0] == 'print':
            print(result_list)


if __name__ == '__main__':
    main()
