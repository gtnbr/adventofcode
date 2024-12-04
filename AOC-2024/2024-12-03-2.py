with open('AOC-2024-3.txt', 'r') as f:
    s = ""
    for l in f:
        x = str(l)
        s += x

def mul_thing(s):
    my_list = []
    current_mul_index = -1
    for i in range(s.count("mul(")):
        current_mul_index = s.find("mul(", current_mul_index+1)
        next_bracket = s.find(")", current_mul_index+1)
        l = s[current_mul_index+4:next_bracket]
        try:
            n1, n2 = map(int, l.split(","))
            my_list.append((n1, n2))
        except:
            continue

    answer = 0
    for i in my_list:
        answer += i[0]*i[1]

    return answer

def do_thing(s):
    answer = 0
    current_do_index = -1
    answer += mul_thing(s[:min(s.index("do()"), s.index("don't()"))])
    print(s[:min(s.index("do()"), s.index("don't()"))])
    print("\n")
    while True:
        current_do_index = s.find("do()", current_do_index + 1)
        if current_do_index == -1:
            break
        next_dont = s.find("don't()", current_do_index + 1)
        if next_dont == -1:
            l = s[current_do_index:]
            print(s[current_do_index:])
            print("\n")
        else:
            l = s[current_do_index:next_dont]
            print(s[current_do_index:next_dont])
        answer += mul_thing(l)
        current_do_index = next_dont+7
        if next_dont == -1:
            break
    return answer

print(do_thing(s))
