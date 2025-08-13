# ================ (Python OOPs concenpt) ================
# There are 3 types fo class ->
# 1) Default Constructor
# 2) Parameterized Constructor
# 3) Default Value Constructor

# # 1) [Default Constructor] =============================
# class Car:
#     def __init__(self):
#         self.brand = ""
#         self.model = ""

# car1 = Car()
# car1.brand = "Toyota Supra"
# car1.model = "Mk4"
# print(f"Car Brand: {car1.brand} And Car Model: {car1.model}") # Car Brand: Toyota Supra And Car Model: Mk4
# ========================================================

# # 2) [Parameterized Constructor] =======================
# class Car:
#     def __init__(self, brand, model):
#         self.Brand = brand
#         self.Model = model

# car1 = Car("Toyota Supra", "MK4")
# car2 = Car("BMW", "M4")
# print(f"1st Cars Brand: {car1.Brand} And Cars  Model: {car1.Model}") # 1st Cars Brand: Toyota Supra And Cars  Model: MK4
# print(f"2nd Cars Brand: {car2.Brand} And Cars  Model: {car2.Model}") # 2nd Cars Brand: BMW And Cars  Model: M4
# ========================================================

# # 3) [Default Value Constructor] =======================
# class Car:
#     def __init__(self, brand="Toyota", model="MK4"):
#         self.Brand = brand
#         self.Model = model

# car1 = Car("BMW", "M4")
# car2 = Car() # Accept the default value
# print(f"Car1 Brand: {car1.Brand} And Model: {car1.Model}") # Car1 Brand: BMW And Model: M4
# print(f"Car2 Brand: {car2.Brand} And Model: {car2.Model}") # Car2 Brand: Toyota And Model: MK4 


# # [Association] ========================================
# # Studen, Laptop
# class Laptop:
#     def __init__(self, Lp_brand):
#         self.Lp_brand = Lp_brand
        
# class Student:
#     def __init__(self, name, laptop_obj):
#         self.stu_name = name
#         self.laptop_v = laptop_obj
#     def show_laptop_info(self):
#         print(f"{self.stu_name} have a {self.laptop_v.Lp_brand}")
#         # Output -> Rafi have a MacBook

# lp1 = Laptop("MacBook")
# student = Student("Rafi", lp1)
# student.show_laptop_info()

# ========================================================


# ========================================================
# class Employee:
#     company_name = "Learn with rafi"
#     def __init__(self, name, salary):
#         self.name = name
#         self._salary = salary

#     @property
#     def get_salary(self):
#         return self._salary

# ob1 = Employee("Rahim", 40000)
# print(ob1._salary) # 40000
# print(ob1.get_salary) # 40000
# ========================================================

# ========================================================
# class Employee:
#     company_name = "Learn with rafi"
#     def __init__(self, name, salary):
#         self.name = name
#         self._salary = salary

#     @property
#     def salary (self):
#         return self._salary
#     @salary.setter
#     def salary(self, new_salary):
#         self._salary = new_salary

# ob1 = Employee("Rahim", 40000)
# print(ob1._salary) # 40000
# ob1.salary = 70000
# print(ob1._salary) # 70000
# ========================================================

# ========================================================
# class Department:
#    def __init__(self, name):
#        self.department_name = name

# class University:
#     def __init__(self, name):
#         self.university_name = name
#         self.departments_list = []
#     def add_department(self, department_obj):
#         self.departments_list.append(department_obj)

#     def show_departments(self):
#         return [department_obj.name for department_obj in self.departments_list]
#     # def show_university(self):
#     #     print(f"University: {self.university_name}")


# un1 = University("BUET")
# dep1 = Department("CSE")
# dep2 = Department("EEE")
# un1.add_department(dep1)
# un1.add_department(dep2)
# print(un1.show_departments())
# # print(un1.show_university())
# ========================================================

# ========================================================
# There are 4-types of principal in OOPs
# 1. Inheritance
# 2. Polimorphism
# 3. Abstraction
# 4. Encapsulation

# ============= (Inheritance) ============================
#[Single-Inheritance] ====================================
# class Grand_father:
#     def __init__(self, fav_color, first_name):
#         self.fav_color = fav_color
#         self.first_name = first_name

# class Father(Grand_father):
#     def __init__(self, hobby, fav_color, first_name):
#         super().__init__(fav_color, first_name)
#         self.hobby = hobby

# Gf1 = Grand_father("Red", "Chowdhuri")
# F1 = Father("Cricket", "Blue", "Rafi")

# print(Gf1.first_name, Gf1.fav_color)
# print(f"Name: {F1.first_name}, Favorit-Color: {F1.fav_color}, Hobby: {F1.hobby}")
# ========================================================

# # [Multiple-Inheritance] ===============================
# # Parent-1
# class Father:
#     def skill_1(self):
#         print("I can Drive")
# # Parent-2
# class Mother:
#     def skill_2(self):
#         print("I can Cook")
# # Child
# class Child(Father, Mother):
#     pass

# c = Child()
# c.skill_1() # From Father - I can Drive
# c.skill_2() # From Mother - I can Cook
# ========================================================

# # [MultiLevel Inheritance] =============================
# # Level-1 (Grandfather)
# class Grandfather:
#     def house(self):
#         print("I have a house")
# # Level-2 (Parents)
# class Father(Grandfather):
#     def Car(self):
#         print("I have a Car")
# # Lavel-3 (Child) 
# class Son(Father):
#     def Bike(self):
#         print("I have a Bike")
# S = Son()
# S.house() # I have a house
# S.Car() # I have a Car 
# S.Bike() # I have a Bike
# =======================================================

# # [Hirarchical inheritance]============================
# # Parents
# class Parent:
#     def home(self):
#         print("We live in the same House.")
# # Child-1
# class Son(Parent):
#     def play_game(self):
#         print("I play video game")
# # CHild-2
# class Daughter(Parent):
#     def read_book(self):
#         print("I love reading book.")
# # Objects
# s = Son()
# d = Daughter()
# s.home() # We live in the same House.
# s.play_game() # I play video game
# d.home() # We live in the same House
# d.read_book() # I love reading book.
# # =====================================================

# # [Hybrid inheritance]=================================
# # Base class -> Level-1
# class Grandfather:
#     def wisdom(self):
#         print("I shere wisdom.")
# # Level-2
# class Father(Grandfather):
#     def car(self):
#         print("I have a Car.")
# class Mother(Grandfather):
#     def cooking(self):
#         print("I can cook")
# # Level-3 -> child inherited from both
# class Child(Father, Mother):
#     def play(slef):
#         print("I play Football.")
# # Objects ->
# c = Child()
# c.wisdom() # I shere wisdom.
# c.car() # I have a Car.
# c.cooking() # I can cook
# c.play() # I play Football.
# # ======================================================

# ## [Encapsulations] ====================================
# class Bank_account:
#     def __init__(self, balance):
#         self.__balance = balance # '__' means --> 'Privet', thats means '__balance' --> 'Privet value'
#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#         else: 
#             print("Deposit amount must be privet!")
#     def get_balance(self):
#         return self.__balance
    
# bank = Bank_account(70000)
# print(f"Old amount: {bank.get_balance()}") # 70000
# bank.deposit(3000) # 70000 + 3000
# print(f"New amount: {bank.get_balance()}") # 73000
# print(bank.__balance) # Error: Can't access directly
# ========================================================

# # [Abstraction] ========================================
# from abc import ABC, abstractmethod

# class PaymentMethod(ABC):
#     @abstractmethod
#     def Pay(self, amount):
#         pass

# class CreditCard(PaymentMethod):
#     def Pay(self, amount):
#         print(f"Paid {amount} using Credit Card 💳")

# class PayPal(PaymentMethod):
#     def Pay(self, amount):
#         print(f"Paid {amount} using PayPal 🅿")

# # # Method-1:
# # method1 = CreditCard()
# # method2 = PayPal()
# # method1.Pay(3000)# Paid 3000 using Credit Card 💳
# # method2.Pay(7000)# Paid 7000 using PayPal 🅿   
# # # Method-2:
# # method = [CreditCard(), PayPal()]
# # for m in method:
# #     m.Pay(5000)
# # # Paid 5000 using Credit Card 💳
# # # Paid 5000 using PayPal 🅿  
# ========================================================

# ## [Singleton Design Pattern] ==========================
# class Singleton:
#     _instance = None # Class variable

#     def __new__(cls):
#         if cls._instance is None:
#             print("1st Object is created!")
#             cls._instance = super(Singleton, cls).__new__(cls)
#         return cls._instance

# # Testing
# obj1 = Singleton() # 1st Object is created!
# obj2 = Singleton() # no output

# print(obj1 is obj2)  # True
# ========================================================

# ## [Factory Design Pattern] ============================
# class Car:
#     def driver(self):
#         return "Driving a Car"
# class Bike:
#     def driver(self):
#         return "Driving a Bike"
# class VahicleFactory:
#     @staticmethod
#     def get_vehicle(type):
#         if type == "car":
#             return Car()
#         elif type == "bike":
#             return Bike()
#         else:
#             return ValueError("Unknown Vehicles!")

# vehicle1 = VahicleFactory.get_vehicle("car")
# vehicle2 = VahicleFactory.get_vehicle("bike")
# print(vehicle1.driver()) # Driving a Car
# print(vehicle2.driver()) # Driving a Bike
# ========================================================

# # [Builder Design Pattern] =============================
# # Definition: Create complex objects step-by-step instead of using one big constructor.
# """ 
# When to use?:
# 1. Many optional parameters
# 2. Flexible object creation
# 3. Complex construction logic
# """
# # Product
# class PC:
#     def __init__(self):
#         self.processor = None
#         self.gpu = None
#         self.ram = None
#         self.ssd = None
#     def __str__(self):
#         return f"CPU: {self.processor}, GPU: {self.gpu}, RAM: {self.ram}, SSD: {self.ssd}"

# # Builder
# class PCBuilder:
#     def __init__(self): self.pc = PC()
#     def add_processor(self, cpu): self.pc.processor = cpu; return self
#     def add_gpu(self, gpu): self.pc.gpu = gpu; return self
#     def add_ram(self, ram): self.pc.ram = ram; return self
#     def add_ssd(self, ssd): self.pc.ssd = ssd; return self
#     def build(self): return self.pc

# # Client
# pc = PCBuilder().add_processor("Intel i9").add_gpu("RTX 4090").add_ram("32GB").add_ssd("1TB").build()
# print(pc) # CPU: Intel i9, GPU: RTX 4090, RAM: 32GB, SSD: 1TB
# # =======================================================