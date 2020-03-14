def extractTime(line, list):
    # print('Hi')
    seconds = 0
    factor = 0.001
    i = -2
    while True:
        i -= 1
        if line[i] == 'm':
            break
        elif line[i] == '.':
            continue
        else:
            seconds += float(line[i])*factor
            factor *= 10

    factor = 60
    while True:
        i -= 1
        if line[i] == ' ':
            break
        else:
            seconds += float(line[i])*factor
            factor *= 10
    list.append(round(seconds,3))
    # Due to inaccuracy of float, sometimes 3e-17 was added.


def main():
    print('Hello')

    real = []
    user = []
    sys = []
    with open('timestat.txt', 'r') as timestat_data:
        for line in timestat_data:
            if line[0] == 'r':
                extractTime(line, real)
            elif line[0] == 'u':
                extractTime(line, user)
            elif line[0] == 's':
                extractTime(line, sys)
    print(real)
    print(sys)
    print(user)

if __name__ == '__main__':
    main()
