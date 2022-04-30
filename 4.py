def remove_punc(string):
    whitelist = set(' 123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    answer = ''.join(filter(whitelist.__contains__, string))
    return answer

import sys

# get the amount of cases
cases = int(sys.stdin.readline().rstrip())

for i in range(cases):

    line = sys.stdin.readline().rstrip()


    print(remove_punc(line))