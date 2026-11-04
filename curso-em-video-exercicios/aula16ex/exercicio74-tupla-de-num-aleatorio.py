import random

num_ale = tuple(random.randint(1, 10) for i in range(10))
num_ali = sorted(num_ale)


print(num_ale)
print(num_ali)
print(max(num_ale))
print(min(num_ali))