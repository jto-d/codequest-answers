import sys

# get the amount of cases
cases = int(sys.stdin.readline().rstrip())

for i in range(cases):
    l = int(sys.stdin.readline().rstrip())

    lines = [sys.stdin.readline().rstrip() for j in range(l)]

    
    
    split = [line.split(",") for line in lines]

    spl = []
    for line in split:
        if line[4] != "false":
            spl.append(line)
    dct = {}
    for line in spl:
        if line[3] not in dct.keys():
            mi = [0,0]
            dct[line[3]] = mi
            if line[2] == "Day":
                mi[0] += 1
            else:
                mi[1] += 1
        else:
            if line[2] == "Day":
                dct[line[3]][0] += 1
            else:
                dct[line[3]][1] += 1
    
    for key in sorted(dct.keys()):
        print(f"{key},{dct[key][0]},{dct[key][1]}")

        

    
