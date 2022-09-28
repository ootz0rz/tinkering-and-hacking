def fizzBuzz(i):
    # Write your code here

    for n in range(1, i):
        is_multi = False

        if n % 3 == 0:
            print("Fizz", end="")
            is_multi = True

        if n % 5 == 0:
            print("Buzz", end="")
            is_multi = True

        if not is_multi:
            print(n)
        else:
            print()


if __name__ == "__main__":
    fizzBuzz(15)
