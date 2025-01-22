def isKaprekar(number) -> bool:
    

    if number < 10:
        return False

    square = str(number ** 2)
    length = len(square)
    
    for i in range(1, length):
        left = square[:i]
        right = square[i:]
        if int(left) + int(right) == number:
            return True
        
    return False


def rangeKaprekar(n):

    kaprekar_nums = []

    for i in range(10, n + 1):
        if isKaprekar(i):
            kaprekar_nums.append(i)

    print("Kaprekar numbers from 10 to", n, "are:", kaprekar_nums)

try:
    user_input = int(input("Enter a number greater or equal to 10: "))
    if user_input < 10:
        print("Please enter a number greater or equal to 10")
    else:
        rangeKaprekar(user_input)
except ValueError:
    print("Please enter a valid integer")