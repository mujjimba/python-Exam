# (i) python program that prints the following patterns
# 1
print("1")
# 12
print("12")
# 128
print("123")
# 1234
print("1234")
# 12345
print('12345')


# (ii) Calculate the factorial of a given number n
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Testing with n = 5
result = factorial(5)
print(result)




#(iii) Testin with a=3 and b=4
def sum_of_numbers(a, b):
    return a + b

result = sum_of_numbers(3, 4)
print(result)



# (iv) 
class Car:
    def __init__(self, brand, year)  :
        self.brand = brand
        self.year = year
        
    def display_info(self):
        print(f"Brand: {self.brand}")  
        print(f"Year: {self.year}")
# creating an instance for the car class
car1 = Car("Benz", 2020)

# Displaying the information about the car
car1.display_info()



# (v) Creating an instance of the class an display the information   
class Car:
    def __init__(self, brand, year)  :
        self.brand = brand
        self.year = year
        
    def display_info(self):
        print(f"Brand: {self.brand}")  
        print(f"Year: {self.year}")

car1 = Car("Benz", 2020)

# Displaying the information about the car
car1.display_info()
      
        