with open('AOC-2024-2.txt', 'r') as f:
    my_list = []
    for l in f:
        x = list(map(int, l.strip().split()))
        my_list.append(x)

def isValid(l):
    if not (l == sorted(l) or l == sorted(l, reverse=True)):
        return False
    for i in range(len(l)-1):
        d = abs(l[i]-l[i+1])
        if d > 3 or d < 1:
            return False
    return True

def Tolorance1(l):
    for i in range(len(l)):
        new_list = l[:i] + l[i+1:]  # Remove the i-th element
        if isValid(new_list):
            return True
    return False

counter = 0

for x in my_list:
    if isValid(x) or Tolorance1(x):
        counter += 1

print(counter)