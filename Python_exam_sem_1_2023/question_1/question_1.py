# write a python named "calculate_area"


















# (ii) 
def natural_numbers(n):
    if n == 0:
        return 1
    else:
        return n * natural_numbers(n-1)

# Testing with n = 4
result = natural_numbers(4)
print(result)



# (iii) Remove the element at index 2
my_list = [1, 3, 5, 7, 9]
my_list.pop(2) 

 # Add 10 at the end of the list 
my_list.append(10)  
print(my_list)


# (iv) New list containing only even numbers
Original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
New_list = [number for number in Original_list if number % 2 == 0]


# (V) 
student_info = {'name': 'Alice', 'age': 20, 'grade': 'A'}
student_info['age'] = 25
student_info['city'] = 'New York'