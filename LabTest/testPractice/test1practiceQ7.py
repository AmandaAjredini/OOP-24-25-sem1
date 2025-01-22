def sumSquares(num: int) -> int:
    """Calculates the sum of the squares of the digits of a number."""

    num_str = str(num)
    sum = 0

    for digit in num_str:
         sum += int(digit) ** 2

    return sum


def isHappy(num: int) -> bool:
    """Check if a number is happy."""

    while True:
         num_squared = sumSquares(num)
         if num_squared == 1:
              return True
         if num_squared == 4:
              return False
         
         num = num_squared
         


def happy_numbers_up_to(num: int) -> None:
    """Print all happy numbers from 1 to n."""

    print("Happy numbers from 1 to ", str(num), " : ")

    for i in range(1, num):
        if isHappy(i):
            print(i, end=' ')



user_input = int(input("Enter a positive integer: "))

if user_input < 1:
        print("Please enter a positive integer greater than 0.")
else:
        happy_numbers_up_to(user_input)