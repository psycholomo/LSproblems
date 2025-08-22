def reciprocal(num):
    counter = 1

    while counter < num:
        yield 1 /counter
        counter += 1

for num in reciprocal(10):
    print(num)

