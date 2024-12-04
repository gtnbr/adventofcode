with open('AOC-2024-1.txt', 'r') as f:
    my_list = []
    my_list1 = []
    my_list2 = []
    for l in f:
        n1, n2 = map(int, l.split())
        my_list1.append(n1)
        my_list2.append(n2)
    for i in range(len(my_list1)):
        my_list.append((sorted(my_list1)[i], sorted(my_list2)[i]))
answer = 0
for t in my_list:
    answer += abs(t[0]-t[1])
print(answer)

# CHATGPT SHORTER VERSION:
# with open('AOC-2024-1.txt', 'r') as f:
#     pairs = [tuple(map(int, l.split())) for l in f]
# sorted_pairs = list(zip(sorted(p[0] for p in pairs), sorted(p[1] for p in pairs)))
# answer = sum(abs(a - b) for a, b in sorted_pairs)
# print(answer)

# Wtf...
# print(sum(abs(a - b) for a, b in zip(*map(sorted, zip(*[map(int, l.split()) for l in open('AOC-2024-1.txt')])))))
