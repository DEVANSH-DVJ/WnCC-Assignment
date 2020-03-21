'''
    Works both for python2 and python3.
    Basic Algorithm:
     1. Read necessary lines as string(char array)
     2. Extract the time in that line as seconds and store it in a list.
     3. Evaluate the lists to get the required results.

    Functions 'extractTimeExtensive' and 'extractTime' have the same purpose.
     However, the former is slower but safer as trailing spaces wouldn't cause an issue.

    Pre-defined function round is being used,
     due to inaccuracy of float (trailing decimal places might not be zero).
'''

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

def analyzeTime(list):
    num = len(list)
    total = 0.0
    mean = 0.0
    variance_numerator = 0.0
    std_dev = 0.0

    for i in range(len(list)):
        total += list[i]

    mean = total / num
    mean = round(mean, 3)

    for i in range(len(list)):
        variance_numerator += (list[i] - mean)**2

    std_dev = (variance_numerator / num)**(0.5)
    std_dev = round(std_dev, 3)

    count = 0
    for i in range(len(list)):
        if (list[i] >= mean - std_dev) and (list[i] <= mean + std_dev):
            count += 1

    return (mean, std_dev, count)

def main():
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

    no_of_runs = len(real)

    real = analyzeTime(real)
    user = analyzeTime(user)
    sys = analyzeTime(sys)

    print("Total number of runs: " + str(no_of_runs))
    print("\nAverage Time Statistics:")
    print("real " + str(real[0]) + "s")
    print("user " + str(user[0]) + "s")
    print("sys  " + str(sys[0]) + "s")
    print("\nStandard deviation of Time statistics:")
    print("real " + str(real[1]) + "s")
    print("user " + str(user[1]) + "s")
    print("sys  " + str(sys[1]) + "s")
    print("\nNumber of runs within average - standard deviation to average + standard deviation:")
    print("real " + str(real[2]))
    print("user " + str(user[2]))
    print("sys  " + str(sys[2]))

if __name__ == '__main__':
    main()
