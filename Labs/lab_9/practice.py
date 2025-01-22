# class Vehicle(object):
#     def __init__(self, model_year, mileage, vin, engine, transmission):
#         self.model_year = model_year
#         self.mileage = mileage
#         self.vin = vin
#         self.engine = engine
#         self.transmission = transmission
    
#     def __str__(self):
#         return {
#             "Model Year": self.model_year,
#             "Mileage": self.mileage,
#             "VIN": self.vin,
#             "Engine": self.engine,
#             "Transmission": self.transmission,
#         }

# class Car(Vehicle):
#     def __init__(self, model_year, mileage, vin, engine, transmission, number_of_doors=4, fuel_efficiency=None, sunroof=False, sports_package=False):
#         # Explicitly call the Vehicle constructor
#         Vehicle.__init__(self, model_year, mileage, vin, engine, transmission)
#         self.number_of_doors = number_of_doors
#         self.fuel_efficiency = fuel_efficiency
#         self.sunroof = sunroof
#         self.sports_package = sports_package

#     def __str__(self):
#         return Vehicle.__str__(self) | {
#             "Number of Doors": self.number_of_doors,
#             "Fuel Efficiency (mpg)": self.fuel_efficiency,
#             "Sunroof": self.sunroof,
#             "Sports Package": self.sports_package,
#         }
    
# class Truck(Vehicle):
#     def __init__(self, model_year, mileage, vin, engine, transmission, payload_capacity=None, tow_capacity=None, off_road_package=False):
#         Vehicle.__init__(self, model_year, mileage, vin, engine, transmission)
#         self.payload_capacity = payload_capacity
#         self.tow_capacity = tow_capacity
#         self.off_road_package = off_road_package

#     def __str__(self):
#         return Vehicle.__str__(self) | {
#             "Payload Capacity (lbs)": self.payload_capacity,
#             "Tow Capacity (lbs)": self.tow_capacity,
#             "Off-Road Package": self.off_road_package,
#         }

# class SUV(Vehicle):
#     def __init__(self, model_year, mileage, vin, engine, transmission, offroad_capability=False, seating_capacity=5, panoramic_sunroof=False):
#         Vehicle.__init__(self, model_year, mileage, vin, engine, transmission)
#         self.offroad_capability = offroad_capability
#         self.seating_capacity = seating_capacity
#         self.panoramic_sunroof = panoramic_sunroof

#     def __str__(self):
#         return Vehicle.__str__(self) | {
#             "Offroad Capability": self.offroad_capability,
#             "Seating Capacity": self.seating_capacity,
#             "Panoramic Sunroof": self.panoramic_sunroof,
#         }


# class Minivan(Vehicle):
#     def __init__(self, model_year, mileage, vin, engine, transmission, sliding_doors=True, cargo_space=None, rear_entertainment_system=False):
#         Vehicle.__init__(self, model_year, mileage, vin, engine, transmission)
#         self.sliding_doors = sliding_doors
#         self.cargo_space = cargo_space
#         self.rear_entertainment_system = rear_entertainment_system

#     def __str__(self):
#         return Vehicle.__str__(self) | {
#             "Sliding Doors": self.sliding_doors,
#             "Cargo Space (cubic feet)": self.cargo_space,
#             "Rear Entertainment System": self.rear_entertainment_system,
#         }


# # Example Instances
# car = Car(2020, 15000, "1HGCM82633A123456", "2.0L 4-Cylinder", "Automatic", 4, 32, sunroof=True, sports_package=True)
# truck = Truck(2018, 50000, "1FTFW1EF5BFA12345", "5.0L V8", "Automatic", 2000, 12000, off_road_package=True)
# suv = SUV(2021, 10000, "5YJXCBE22MF000123", "Electric", "Single Speed", True, 7, panoramic_sunroof=True)
# minivan = Minivan(2019, 30000, "2C4RC1BG3KR512345", "3.6L V6", "Automatic", True, 140, rear_entertainment_system=True)



# class BankAccount(object):
#     def __init__(self, iban, accNo, balance=0):
#         """Initializes the bank account with IBAN, account number, and an initial balance."""
#         self.iban = iban
#         self.accNo = accNo
#         self.balance = balance
#         self.transactions = []  # To store the last 5 transactions

#     def deposit(self, amount):
#         """Deposits money into the account and logs the transaction."""
#         if amount > 0:
#             self.balance += amount
#             self.transactions.append(f"Deposited: {amount}")
#             self._log_transaction()
#         else:
#             print("Deposit amount must be positive.")

#     def withdraw(self, amount):
#         """Withdraws money from the account and logs the transaction if sufficient funds are available."""
#         if amount > 0:
#             if amount <= self.balance:
#                 self.balance -= amount
#                 self.transactions.append(f"Withdrew: {amount}")
#                 self._log_transaction()
#             else:
#                 print("Insufficient funds.")
#         else:
#             print("Withdrawal amount must be positive.")

#     def _log_transaction(self):
#         """Keeps only the last 5 transactions in the transaction history."""
#         if len(self.transactions) > 5:
#             self.transactions.pop(0)

#     def get_transactions(self):
#         """Returns the list of the last 5 transactions."""
#         return self.transactions

#     def __str__(self):
#         """Returns a string representation of the bank account."""
#         return f"Bank Account {self.accNo} (IBAN: {self.iban})\n" \
#                f"Balance: {self.balance}\n" \
#                f"Last Transactions: {', '.join(self.transactions)}"
    
# class MinimumBalanceAccount(BankAccount):
#     def __init__(self, iban, accNo, balance=0, minimum_balance=0):
#         BankAccount.__init__(self, iban, accNo, balance)
#         self.minimum_balance = minimum_balance

#     def withdraw(self, amount):
#         """Withdraws money only if the balance after withdrawal doesn't fall below the minimum balance."""
#         if self.balance - amount >= self.minimum_balance:
#             self.balance -= amount
#             self.transactions.append(f"Withdrew: {amount}")
#             self._log_transaction()
#             print(f"Withdrawal successful. New balance: {self.balance}")
#         else:
#             print(f"Cannot withdraw {amount}. Balance cannot drop below the minimum balance of {self.minimum_balance}.")


# # main()
# acc1 = BankAccount("IEPBS32435354353", 3745325, 200)
# print(acc1, "\n")
# acc1.deposit(200)
# acc1.withdraw(50)
# print(acc1, "\n")


# # Create an instance of MinimumBalanceAccount
# min_balance_account = MinimumBalanceAccount("IE29AIBK93115212345678", "12345678", balance=1000, minimum_balance=200)

# # Display account information
# print(min_balance_account)

# # Test deposits
# min_balance_account.deposit(300)
# print(min_balance_account)

# # Test valid withdrawal (balance stays above the minimum)
# min_balance_account.withdraw(800)
# print(min_balance_account)

# # Test invalid withdrawal (balance would drop below the minimum)
# min_balance_account.withdraw(400)
# print(min_balance_account)

# # Display transaction history
# print("Last 5 transactions:", min_balance_account.get_transactions())

# class Meeting:
#     total_meetings = 0  # Tracks total number of meetings

#     def __init__(self):
#         """Initializes a new meeting with 0 attendees."""
#         self.attendees = 0
#         Meeting.total_meetings += 1
#         print(f"Welcome to Meeting #{Meeting.total_meetings}!")
#         print(f"Current attendees: {self.attendees}")

#     def join(self, count=1):
#         """Adds attendees to the meeting."""
#         self.attendees += max(0, count)  # Ensures only positive counts are added
#         self.display_attendees()

#     def leave(self, count=1):
#         """Removes attendees from the meeting."""
#         self.attendees -= min(self.attendees, max(0, count))  # Ensures attendees don’t go below 0
#         self.display_attendees()

#     def display_attendees(self):
#         """Displays the current number of attendees."""
#         print(f"Current attendees: {self.attendees}")


# # Example Program
# meeting1 = Meeting()  # New meeting
# meeting1.join(3)      # 3 people join
# meeting1.leave(1)     # 1 person leaves
# meeting1.leave(10)    # Attempt to remove more attendees than present

# meeting2 = Meeting()  # Another meeting
# meeting2.join(5)      # 5 people join



# class Student:
#     """
#     This class represents a student with personal and academic details.

#     """

#     POSTGRADUATE = "Postgraduate"
#     UNDERGRADUATE = "Undergraduate"

#     def __init__(self, study_type, f_name, l_name):
#         self.study_type = study_type
#         self.f_name = f_name
#         self.l_name = l_name
#         self.courses = []
    
#     def set_courses(self, course_name):
#         """
#         Adds a course to the student's list of courses.

#         """
#         self.courses.append(course_name)

   
#     def __str__(self):
#         result_str = ""
#         result_str += f"{self.f_name} {self.l_name}\n"
#         result_str += f"Type: {self.study_type}\n"
#         result_str += f"Courses: {', '.join(self.courses)}"

#         return result_str


# class RegistrationData:
#     """
#     This class represents a student's registration data, including their personal details 
#     and registration information.
#     """
#     def __init__(self, address, registration_fee, study_type, f_name, l_name, s_id="NA"):
#        self.address = address
#        self.registration_fee = registration_fee
#        self.s_id = s_id

#        self.student = Student(study_type, f_name, l_name)

#     def display_student_data(self):
#         print(self.student)
#         print(f"ID: {self.s_id}")
#         print(f"Address: {self.address}")
#         print(f"Registration Fee: €{self.registration_fee}")

#     def get_student_object(self):
#         """
#         Returns the student object associated with this registration.
#         """
#         return self.student

#     def set_student_id_property(self, new_id):
#         self.s_id = new_id



# # MAIN SCOPE - UNCOMMENT IT AND RUN AFTER IMPLEMENTING YOUR SOLUTION
# r = RegistrationData("8 Lower Kevin Street, Dublin 8, Ireland", 1500,
#                      Student.POSTGRADUATE, "Lucas", "Rizzo")
# r.display_student_data()
# print()
# r.set_student_id_property("C12345")
# r.display_student_data()
# print()
# for course in ("OOP", "Advanced Databases", "Environmental Analytics"):
#     r.get_student_object().set_courses(course)

# r.display_student_data()
# print()
# print(r.get_student_object())  # extra to match the __str__ additional function
# print()
# print(RegistrationData.__doc__)


# from datetime import datetime

# class Gym(object):
#     """
#     This class represents a gym with multiple members and equipment.
#     """
#     def __init__(self, gym_name):
#         """
#         Initialize a gym with its name and empty lists for members and equipment.
#         """
#         self.gym_name = gym_name
#         self.members = []
#         self.equipment_list = []

#     def add_member(self, member):
#         """
#         Adds a member to the gym.
#         """
#         self.members.append(member)

#     def add_equipment(self, equipment):
#         """
#         Adds equipment to the gym.
#         """
#         self.equipment_list.append(equipment)

#     def __str__(self):
#         """
#         Returns a string representation of the gym's details.
#         """
#         members_str = ""
#         if self.members:
#             for member in self.members:
#                 members_str += str(member) + "\n"
#         else:
#             members_str = "No members yet."

#         equipment_str = ""
#         if self.equipment_list:
#             for equipment in self.equipment_list:
#                 equipment_str += str(equipment) + "\n"
#         else:
#             equipment_str = "No equipment available."

#         return (f"Gym Name: {self.gym_name}\n\nMembers:\n{members_str if self.members else 'No members yet.'}\n\n"
#                 f"Equipment:\n{equipment_str if self.equipment_list else 'No equipment available.'}")


# class Equipment(object):
#     """
#     This class represents a piece of gym equipment.
#     """
#     def __init__(self, name, category, status="Available"):
#         """
#         Initialize equipment with a name, category, and status.
#         """
#         self.name = name
#         self.category = category
#         self.status = status

#     def __str__(self):
#         """
#         Returns a string representation of the equipment's details.
#         """
#         return f"Equipment: {self.name} ({self.category}) - Status: {self.status}"

# class Member(object):
#     """
#     This class represents a gym member.
#     """
#     def __init__(self, name, membership_type, membership_start_date):
#         """
#         Initialize a gym member with their personal details and membership type.
#         """
#         self.name = name
#         self.membership_type = membership_type
#         self.membership_start_date = datetime.strptime(membership_start_date, "%Y-%m-%d")
#         self.equipment_used = []

#     def use_equipment(self, equipment):
#         """
#         Allows a member to use a piece of equipment.
#         """
#         if equipment.status == "Available":
#             self.equipment_used.append(equipment)
#             equipment.status = "In use"
#             print(f"{self.name} is using {equipment.name}.")
#         else:
#             print(f"Sorry, {equipment.name} is currently unavailable.")

#     def __str__(self):
#         """
#         Returns a string representation of the member's details.
#         """
#         equipment_names = [eq.name for eq in self.equipment_used]
#         return (f"Member: {self.name}\nMembership Type: {self.membership_type}\n"
#                 f"Membership Start Date: {self.membership_start_date.strftime('%Y-%m-%d')}\n"
#                 f"Equipment Used: {', '.join(equipment_names) if equipment_names else 'No equipment used'}\n")

# # Instantiate the Gym, Equipment, and Members

# # Create a gym
# my_gym = Gym("FitLife Gym")

# # Add equipment to the gym
# treadmill = Equipment("Treadmill", "Cardio")
# dumbbells = Equipment("Dumbbells", "Strength")
# stationary_bike = Equipment("Stationary Bike", "Cardio")
# my_gym.add_equipment(treadmill)
# my_gym.add_equipment(dumbbells)
# my_gym.add_equipment(stationary_bike)

# # Add members to the gym
# alice = Member("Alice Johnson", "Premium", "2023-06-15")
# bob = Member("Bob Smith", "Basic", "2024-01-05")
# my_gym.add_member(alice)
# my_gym.add_member(bob)

# # Members use equipment
# alice.use_equipment(treadmill)
# bob.use_equipment(dumbbells)
# alice.use_equipment(stationary_bike)

# # Display gym information
# print(my_gym)

###########################################################################
# class NewClass(object):
#    def __init__(self, param_int=1):
#        self.the_int = param_int
#        if param_int % 2 == 0:
#            self.parity = 'even'
#        else:
#            self.parity = 'odd'


#    def process(self, instance):
#        sum_int = self.the_int + instance.the_int
#        if sum_int < 0:
#            return 'negative'
#        elif sum_int % 2 == 0:
#            return 'even'
#        else:
#            return 'odd'


#    def __str__(self):
#        return 'Value {} is {}'.format(self.the_int, self.parity)




# inst1 = NewClass(4)
# inst2 = NewClass(-5)
# inst3 = NewClass()
# print(inst1)  # Line 1
# print(inst1.parity)  # Line 2
# print(inst1.process(inst2))  # Line 3
# print(inst3.process(inst1))  # Line 4


# Q2 a)
# class Rectangle(object):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self) -> float:
#         return (self.length * self.width)

#     def perimeter(self) -> float:
#         '''
#         Returns the perimeter of a rectangle using the arguments length and width.
#         '''
#         return (self.length * 2) + (self.width * 2)
    
#     def __str__(self):
#         return f"Rectangle with length {self.length} and width {self.width}."
    
# r = Rectangle(4, 3)
# print(r.area())
# print(r.perimeter())
# print(r)


# Q2 b)
# class BankAccount(object):
#     def __init__(self, iban: str, accNo: str, balance: int = 0):
#         self.iban = iban
#         self.accNo = accNo
#         self.balance = balance
#         self.transactions = []

#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             self.transactions.append(f"Deposited: {amount}")
#             self.log_transaction()
#         else:
#             print("Please enter a positive amount to deposit!")

#     def withdraw(self, amount):
#         if amount > 0:
#             if amount <= self.balance:
#                 self.balance -= amount
#                 self.transactions.append(f"Withdrew: {amount}")
#                 self.log_transaction()
#             else:
#                  print("Insufficient funds.")
#         else:
#             print("Please enter a positive amount to withdraw!")

#     def log_transaction(self):
#         if len(self.transactions) > 5:
#             self.transactions.pop(0)

#     def get_transactions(self):
#         return self.transactions

#     def __str__(self):
#         return f"Bank Account with Details:\n" \
#                 f"IBAN: {self.iban}\n" \
#                 f"Account Number: {self.accNo}\n" \
#                 f"Balance: {self.balance}\n" \
#                 f"Last 5 Transactions: {', '.join(self.transactions)}\n"
    
# acc = BankAccount("IE32498324ERG435", "12345678")
# acc.deposit(500)
# acc.withdraw(200)
# acc.deposit(1000)
# acc.withdraw(300)
# acc.withdraw(20)
# acc.withdraw(90)
# acc.withdraw(800)

# print(acc)

