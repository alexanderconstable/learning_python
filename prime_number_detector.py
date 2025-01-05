import random


def isprime(number):
    isprime_flag = True
    for c in range(2, number):
        d = number / c
        if d.is_integer():
            isprime_flag = False
    return isprime_flag


def main():
    print("Enter A Number Or Hit Enter To Generate A Random Number: ")

    captured_input = input()

    if captured_input == "q":
        exit()
    elif captured_input == "":
        y = random.randrange(1, 100) + 1
        print(f"RANDOM NUMBER: {y}")
    else:
        y = int(captured_input)

    for b in range(1, y):
        if isprime(b):
            print(f"PRIME NUMBER: {b}")


while True:
    main()
