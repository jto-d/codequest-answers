import sys

# get the amount of cases
cases = int(sys.stdin.readline().rstrip())

for i in range(cases):
    a = sys.stdin.readline().rstrip()
    init = int(a.split(" ")[0])
    fin = int(a.split(" ")[1])

    i = [sys.stdin.readline().rstrip() for j in range(init)]
    f = [sys.stdin.readline().rstrip() for j in range(fin)]

    output = []



    for part in i:
        if part not in f:
            output.append(part)

    if len(output) > 0:    
        for line in output:
            print(line)
