import random
count = 0
while True:
    throw1 = random.randint(1,6)
    throw2 = random.randint(1,6)
    total = throw1 + throw2
    count = count + 1
    print  (total)
    if throw1 == 6 and throw2 == 6:
        break
print('Double Six Thrown!')
print(count,'times')