#Note Генератор
def my_gen(stop):
    i = -1

    while i < stop - 1:
        i += 1
        yield i

    #return

for i in my_gen(5):
    print(i)