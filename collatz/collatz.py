def collatz(n):
    if n % 2 == 0:
        print (n//2)
        return n // 2
    else :
        print((3 * n) + 1)
        return (3 * n) + 1
try:
    number = int(input('Enter a number:'))
except ValueError:
    print('Error: Invalid argument.')

while number != 1:
    number = collatz(number)
