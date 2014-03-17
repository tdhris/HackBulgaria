from random import randint

def generate_numbers(filename, n):
    numbers = [str(randint(1,1000)) for x in range(n)]
    file = open(filename, "w")
    file.write(" ".join(numbers))
    file.close()