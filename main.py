listOfNumbers = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]

oddSquare1Way = list(map(lambda x: x ** 2, filter(lambda x: x % 2, listOfNumbers)))
print(oddSquare1Way)

oddSquare2Way = [x ** 2 for x in listOfNumbers if x % 2]
print(oddSquare2Way)


def squared(num):
    return num ** 2


def odd_number(num):
    return num % 2


oddSquare3Way = list(map(lambda x: squared(x), filter(lambda x: odd_number(x), listOfNumbers)))
print(oddSquare3Way)
