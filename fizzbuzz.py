# "fizzbuzz.py" Is a program that has a range of numbers of 1 - 100 where it
# shows on the terminal the number without anything in front, when the number
# is a multiple of 3 it prints the number and "Fizz" in front, but when the
# number is a multpiple of 5 it prints "Buzz", if they are both multiples
# of 3 and 5 it prints "FizzBuzz". 

nums = range(1, 101)

for num in nums:

    if num % 3 != 0 and num % 5 != 0:
        print(num)

    if num % 3 == 0 and num % 5 == 0:
        print(f"{num} FizzBuzz")

    if num % 3 == 0:
        print(f"{num} Fizz")

    if num % 5 == 0:
        print(f"{num} Buzz")