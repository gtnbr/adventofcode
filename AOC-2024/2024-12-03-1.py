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

print(mul_thing(s))
