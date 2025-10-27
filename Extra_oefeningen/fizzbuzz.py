fizzbuzz = int(input("Give me a number: "))

if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
    print('Fizzbuzz')

elif fizzbuzz % 3 == 0:
    print('Fizz')

elif fizzbuzz % 5 == 0:
    print('Buzz')

else:
    print("You gave the wrong input")