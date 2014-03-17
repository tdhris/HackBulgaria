def sum_numbers(filename):
    file = open(filename, "r")
    numbers = map(lambda x: int(x), file.read().split(" "))
    file.close()
    return sum(numbers)