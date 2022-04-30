import sys

# get the amount of cases
cases = int(sys.stdin.readline().rstrip())

def encrypt(string, dic):
    encoded = [dic[char] for char in string]
    return "   ".join(encoded)

def decrpyt(string, dic):
    decode = ""
    inv_dic = {v: k for k, v in dic.items()}
    no_spaces = string.split("       ")
    for word in no_spaces:
        st = word.split("   ")
        for char in st:
            decode += inv_dic[char]
        decode += " "

    return decode
        


for i in range(cases):
    code = {}

    for line in range(26):
        case = sys.stdin.readline().rstrip()
        code[case[0]] = case[2::]
    
    code[" "] = " "

    enc = sys.stdin.readline().rstrip()
    print(encrypt(enc, code))
    dec = sys.stdin.readline().rstrip()

    
    print(decrpyt(dec, code)[0:-1])

    


    

