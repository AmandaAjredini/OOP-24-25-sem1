def sum_divisors(number):

    if number < 0:
        print("Negative number. Only positive numbers accepted.")
        return

    sum = 0
    divisors = ""

    for i in range(1,number + 1):
        if number % i == 0:
            sum += i
            divisors += str(i) + " + "
    
    divisors = divisors[:-1].strip("+")
    #divisors = divisors[:-3] + " = " + str(sum)

    print(divisors, "=", sum)
    


user_input = int(input("Enter a number to list all of its divisors: "))
sum_divisors(user_input)