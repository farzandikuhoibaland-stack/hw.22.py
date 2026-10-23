# p1
# class Vehicle:
#     def move(self):
#         print('Транспорт движется')

# class Car(Vehicle):
#     def honk(self):
#         print("Би-би!")


# car=Car()
# car.move()
# car.honk()


# p2
# class Employee:
#     def work(self):
#         print("Сотрудник работает")

# class Programmer:
#     def work(self):
#         print("Пишет код")

# class Teacher:
#     def work(self):
#         print("Проводит урок")


# e=Employee()
# e.work()

# p=Programmer()
# p.work()

# t=Teacher()
# t.work()



# p3
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

# class Student(Person):
#     def __init__(self, name, age, group):
#         super().__init__(name, age)
#         self.group=group

#     def info(self):
#         print(f'Student: {self.name}, {self.age}, {self.group}')


# s = Student("Али", 19, "Python-1")
# s.info()


# p4
# class Animal:
#     def speak(self):
#         return("Животное издаёт звук")

# class Cat(Animal):
#     def speak(self):
#         print( super().speak())
#         print("Мяу")
   
# c=Cat()
# c.speak()


# p5
# class Device():
#     def power_on(self):
#         print("Устройство включено")

# class Phone(Device):
#     def call(self,number):
#         print(f"Звоню на номер {number}...")

# class Smartphone(Phone):
#     def take_photo(self):
#         print("Фото сделано")

# s=Smartphone()
# s.power_on()
# s.call('2211')
# s.take_photo()


# p6
# class Flyer:
#     def fly(self):
#         print('I can flyyy')

# class Swimmer:
#     def swim(self):
#         print('i can swimmmm')

# class Duck(Flyer, Swimmer):
#     def quack(self):
#         print('krya')

# d=Duck()
# d.fly()
# d.quack()
# d.swim()




# p7
# class User:
#     def __init__(self,name,email):
#         self.name=name
#         self.email=email

#     def get_info(self):
#         return(f'name: {self.name}, email: {self.email}')

# class Admin(User):
#     def __init__(self, name, email,level):
#         super().__init__(name, email)
#         self.level=level

#     def get_info(self):
#      return(f'{super().get_info()}, level:{self.level}')


# class Customer(User):
#     def __init__(self, name, email,balance):
#         super().__init__(name, email)
#         self.balance=balance

#     def get_info(self):
#        return(f'{super().get_info()}, balance:{self.balance}') 

# class Guest(User):
#     def __init__(self, name, email):
#         super().__init__(name, email)

#     def get_info(self):
#         return super().get_info()
    

# print(Admin("Али", "ali@mail.tj", 3).get_info())
# print(Customer("Soro", "sara@mail.tj", 150.50).get_info())
# print(Guest("eshmat", "john@mail.tj").get_info())


# p8
# class Circle:

#     def __init__(self, r):
#         self.r=r
#         self.p=3.14

#     def area(self):
#         return self.p*(self.r**2)

# class Rectangle:
#     def __init__(self, a, b):
#         self.a=a
#         self.b=b

#     def area(self):
#         return self.a * self.b

# class Triangle:
#     def __init__(self, b, h):
#         self.b=b
#         self.h=h

#     def area(self):
#         return self.b*self.h/2
    
# shapes = [Circle(3), Rectangle(4, 5), Triangle(6, 2)]
# for s in shapes:
#     print(type(s).__name__, s.area())


# p9
# a
# class Calculator:
#     def multiply(self,a, b=1, c=1):
#         print ( a*b*c )

# calc = Calculator()
# calc.multiply(5)        
# calc.multiply(5, 2)     
# calc.multiply(5, 2, 3) 


# b
# from enum import Enum

# class OrderStatus(Enum):
#     NEW = 1
#     PAID = 2
#     SHIPPED = 3
#     DELIVERED = 4
    
#     def next_status(status):
#         if status == OrderStatus.DELIVERED:
#          return status
    
#         return OrderStatus(status.value + 1)

# current = OrderStatus.NEW
# result = current.next_status()

# print(f"Name: {result.name}, Value: {result.value}")


# p10
# from enum import Enum


# class PaymentStatus(Enum):
#     SUCCESS = 1
#     FAILED = 0


# class Payment:
#     def __init__(self, owner):
#         self.owner = owner

#     def pay(self, amount):
#         if amount <= 0:
#             return PaymentStatus.FAILED
#         print("Unknown payment method", end="")
#         return PaymentStatus.FAILED


# class CardPayment(Payment):
#     def __init__(self, owner, card_number):
#         super().__init__(owner)
#         self.card_number = card_number

#     def pay(self, amount):
#         if amount <= 0:
#             return PaymentStatus.FAILED
        
        
#         for i in self.card_number:
#             i==int(self.card_number)%10
#             if len(i)==4:
#                print(f"{self.owner} paid {amount} somoni by card ****{i}", end="")
#         return PaymentStatus.SUCCESS


# class CashPayment(Payment):
#     def __init__(self, owner):
#         super().__init__(owner)

#     def pay(self, amount):
#         if amount <= 0:
#             return PaymentStatus.FAILED
        
#         print(f"{self.owner} paid {amount} somoni in cash", end="")
#         return PaymentStatus.SUCCESS


# class WalletPayment(Payment):
#     def __init__(self, owner, balance):
#         super().__init__(owner)
#         self.balance = balance

#     def pay(self, amount):
#         if amount <= 0:
#             return PaymentStatus.FAILED
        
#         if amount > self.balance:
#             print(f"{self.owner}: not enough money in the wallet", end="")
#             return PaymentStatus.FAILED
        
#         self.balance -= amount
#         print(f"{self.owner} paid {amount} somoni from wallet", end="")
#         return PaymentStatus.SUCCESS



# p = [
#     (CardPayment("Ali", "1234567890124321"), 200),
#     (CashPayment("Vali"), 150),
#     (WalletPayment("Sino", 100), 150) 
# ]

# for payment_method, amount in p:
#     print(f" - {payment_method.pay(amount).name}")


