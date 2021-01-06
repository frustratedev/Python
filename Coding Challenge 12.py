# Coding Challenge 12
# Using the concept of object oriented programming and inheritance, create a super class named Computer, which has two sub classes named Desktop and Laptop.
# Define two methods in the Computer class named getspecs and displayspecs, to get the specifications and display the specifications of the computer.
# You can use any specifications which you want.
# The Desktop class and the Laptop class should have one specification which is exclusive to them for example laptop can have weight as a special specification.
# Make sure that the sub classes have their own methods to get and display their special specification.
# Create an object of laptop/ desktop and make sure to call all the methods from the computer class as well as the methods from the own class

class Computer:
    def __init__(self, ram, cpu, gpu):
        self.ram = ram
        self.cpu = cpu
        self.gpu = gpu

    def get_specs(self):
        self.ram = input("Enter ram: ")
        self.cpu = input("Enter cpu: ")
        self.gpu = input("Enter gpu: ")

    def display_specs(self):
        print(self.ram)
        print(self.cpu)
        print(self.gpu)

class Desktop(Computer):
    def Desktop_Specs(self):
        print("This shows the PC specs")

a = Desktop("", "", "")
a.get_specs()
a.display_specs()
a.Desktop_Specs()

class Laptop():
    def Laptop_Specs(self):
        print("This shows the laptop's specs")

    def __init__(self, ram, cpu, gpu, model):
        self.ram = ram
        self.cpu = cpu
        self.gpu = gpu
        self. model = model

    def get_specs(self):
        self.ram = input("Enter ram: ")
        self.cpu = input("Enter cpu: ")
        self.gpu = input("Enter gpu: ")
        self.model = input("Enter model: ")

    def display_specs(self):
        print(self.ram)
        print(self.cpu)
        print(self.gpu)
        print(self.model)

b = Laptop("", "", "", "")
b.get_specs()
b.display_specs()
b.Laptop_Specs()