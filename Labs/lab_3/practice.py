
def singleInt(my_list):

    result = ""

    for num in my_list:
        result = result + str(num) 

    return int(result)


my_list = [11, 33, 50] 

result = singleInt(my_list)
print(result)