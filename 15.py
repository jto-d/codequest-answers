import sys

# get the amount of cases
cases = int(sys.stdin.readline().rstrip())

def remove_punc(string):
    string = string.upper()
    whitelist = set(' ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    answer = ''.join(filter(whitelist.__contains__, string))
    return answer

def di(lst):
    output = []
    dct = {}
    for line in lst:
        words = line.split(" ")
        for word in words:
            dis = [word[i: j] for i in range(len(word)) for j in range(i + 1, len(word) + 1) if len(word[i:j]) == 2]

            for di in dis:
                if di in dct.keys():
                    dct[di] += 1
                else:
                    dct[di] = 1
    total_dis = sum(dct.values())
    for key in dct.keys():
        percentage = dct[key]/total_dis*100
        # percentage = "%.2f" % round(percentage, 4)
        output.append(f"{key}: {percentage:.3f}%")
    return sorted(output)

def tri(lst):
    output = []
    dct = {}
    for line in lst:
        words = line.split(" ")
        for word in words:
            dis = [word[i: j] for i in range(len(word)) for j in range(i + 1, len(word) + 1) if len(word[i:j]) == 3]

            for di in dis:
                if di in dct.keys():
                    dct[di] += 1
                else:
                    dct[di] = 1
    total_dis = sum(dct.values())
    for key in dct.keys():
        percentage = dct[key]/total_dis*100
        # percentage = "%.2f" % round(percentage, 4)
        output.append(f"{key}: {percentage:.3f}%")
    return sorted(output)
    



for i in range(cases):
    l = int(sys.stdin.readline().rstrip())
    lines = [remove_punc(sys.stdin.readline().rstrip()) for a in range(l)]




    for line in di(lines):
        print(line)
    for line in tri(lines):
        print(line)