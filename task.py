def extractTimeExtensive(line, list):
    minutes = 0
    milliseconds = 0

    i = 3
    min = True
    while True:
        i += 1
        if line[i] == 's':
            break
        elif line[i] == '.' or line[i] == ' ':
            continue
        elif line[i] == 'm':
            min = False
        elif min:
            minutes *= 10
            minutes += float(line[i])
        else:
            milliseconds *= 10
            milliseconds += float(line[i])

    seconds = (minutes * 60) + (milliseconds / 1000)
    list.append(round(seconds, 3))
    # Due to inaccuracy of float, trailing decimal places might not be zero.

# Trailing spaces would cause wrong problems, but it is faster.
def extractTime(line, list):
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
            seconds += float(line[i]) * factor
            factor *= 10

    factor = 60
    while True:
        i -= 1
        if line[i] == ' ':
            break
        else:
            seconds += float(line[i]) * factor
            factor *= 10
    list.append(round(seconds, 3))
    # Due to inaccuracy of float, sometimes 3e-17 was added.

def main():
    print('Hello')

    real = []
    user = []
    sys = []
    with open('timestat.txt', 'r') as timestat_data:
        for line in timestat_data:
            if line[0] == 'r':
                extractTimeExtensive(line, real)
            elif line[0] == 'u':
                extractTimeExtensive(line, user)
            elif line[0] == 's':
                extractTimeExtensive(line, sys)
    print(real)
    print(sys)
    print(user)

if __name__ == '__main__':
    main()
