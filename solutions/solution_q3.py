def find_factorial(number):
    factorial = 1
    if number not in [0, 1]:
        factorial = number * find_factorial(number - 1)
    return factorial


if __name__ == "__main__":
    number = int(input())
    print(find_factorial(number))
