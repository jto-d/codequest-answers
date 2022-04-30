import sys

# get the amount of cases
cases = int(sys.stdin.readline().rstrip())

def conv(num: str):
    new = int(num, 2)
    return chr(new)

for i in range(cases):
    seq = sys.stdin.readline().rstrip()
    output = ""
    bi = ""
    for char in seq:
        if char == "A" or char == "T":
            bi+="0"
        else:
            bi+="1"
    
    split = [bi[x:x+7] for x in range(0, len(bi), 7)]
    
    for num in split:
        output += conv(num)

    print(output)
