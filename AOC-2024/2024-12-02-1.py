with open('AOC-2024-2.txt', 'r') as f:
    my_list = []
    for l in f:
        x = list(map(int, l.split()))
        my_list.append(x)

def isValid(l):
    if not (l == sorted(l) or l == sorted(l, reverse=True)):
        return False
    for i in range(len(l)-1):
        d = abs(l[i]-l[i+1])
        if d > 3 or d < 1:
            return False
    return True

counter = 0
for x in my_list:
    if isValid(x):
        counter +=1

print(counter)