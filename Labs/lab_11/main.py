#
# #Q1
# class TestClass(object):
#
#
#   def __init__(self,param_str=''):
#     self.the_str=''
#     for c in param_str:
#       if c.isalpha():
#         self.the_str += c
#
#
#   def __add__(self,param):
#     if type(param)==TestClass:
#       the_str = self.the_str + param.the_str
#       return TestClass(the_str)
#     else:
#       return self
#
#
#   def __str__(self):
#     return 'Value: {}'.format(self.the_str)
#
#
# inst1 = TestClass('abc')
# inst2 = TestClass('123ijk')
# sumInst1 = inst1 + inst2
# sumInst2 = inst1 + 'xyz'
# print(inst1) # Line 1
# print(sumInst1) # Line 2
# print(sumInst2) # Line 3
# print(isinstance(sumInst2,TestClass)) # Line 4


#(a) What output is produced by # Line 1 of the above program? ->
#(b) What output is produced by # Line 2 of the above program? ->
#(c) What output is produced by # Line 3 of the above program? ->
#(d) What output is produced by # Line 4 of the above program? ->


# class WholeNumber(object):
#     def __init__(self, value=0):
#
#         if not isinstance(value, int) or value < 0:
#             raise ValueError("Whole number must be a non negative integer")
#         else:
#             self.value = value
#
#     def __add__(self, other):
#         if not isinstance(other, WholeNumber):
#             raise ValueError("Whole numbers can only be added with whole numbers")
#
#         return WholeNumber(self.value + other.value)
#
#     def __sub__(self, other):
#         if not isinstance(other, WholeNumber):
#             raise ValueError("Whole numbers can only be subtracted with whole numbers")
#
#
#         return WholeNumber(self.value - other.value)
#
#     def __mul__(self, other):
#         if not isinstance(other, WholeNumber):
#             raise ValueError("Whole numbers can only be multiplied with whole numbers")
#
#         return WholeNumber(self.value * other.value)
#
#     def __str__(self):
#         return f"{self.value}"
#
#
#
# n1 = WholeNumber(5)
# n2 = WholeNumber(3)
#
# n3 = n1 + n2
# print("Addition")
# print(n3)
#
# n3 = n1 - n2
# print("Subtraction")
# print(n3)
#
# n3 = n1 * n2
# print("Multiplication")
# print(n3)


class LinearEquation(object):
    def __init__(self, m, b):
        self.m = m
        self.b = b

    def value(self, x):
        return self.m * x + self.b

    def compose(self, other):

        if not isinstance(other, LinearEquation):
            raise ValueError("Compose only works between linear equations")

        # y = ax + b and z = cx + d,
        # then y(z)= (a*c)x + (a*d + b)

        new_m = self.m * other.m
        new_b = (self.m * other.b) + self.b

        return LinearEquation(new_m, new_b)

    def __add__(self, other):
        if not isinstance(other, LinearEquation):
            raise ValueError("Addition only works between linear equations")

        #y + z = (a + c)x + (b + d)

        new_m = self.m + other.m
        new_b = self.b + other.b

        return LinearEquation(new_m, new_b)


    def __str__(self):
        return f"y = {self.m}x + {self.b}"

# Main Scope
l1 = LinearEquation(3, 2) # y = 3x + 2
print(l1.value(10))

l2 = LinearEquation(5, 3) # y = 5x + 3
l3 = l1.compose(l2) # y = mx + b
l3 = l1 + l2
print(l3)






