import random

y = random.randrange(1, 10)

output = ""
for b in range(10 - y):
    output = output + str(b)
    print(output)