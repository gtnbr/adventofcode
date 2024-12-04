with open('AOC-2024-1.txt', 'r') as f:
    my_list1 = []
    my_list2 = []
    for l in f:
        n1, n2 = map(int, l.split())
        my_list1.append(n1)
        my_list2.append(n2)

score = 0
for i in my_list1:
    score += i*my_list2.count(i)
print(score)