#This code uses a while loop in combination with a nested if-else statement and list functions. 
#It collects numbers given by the user and develops an average of numbers entered.
#It depends on whether the user inputs -1 in order to halt requests for numbers and then display the average.

num_input = () #defining a storable variable for user inputs
num_list = [] #defining a storable list to collect user inputs

while True: #Turns the program on.
    if  num_input != -1: #starting the condition of requesting user inputs.
        num_input = int(input("Please enter a number: "))
        num_list.append(num_input) #collecting and storing user inputs
    else: #if the condition of halting the input collection (-1 being entered) occurs
        break
num_list.remove(-1)  #-1 is excluded from the calculation of the average.

#Calculating the average of user inputs:
num_count = len(num_list) #counting the number of items input
num_sum = sum(num_list) #adding all the inputs together
num_average = num_sum / num_count #dividing number of inputs by sum of inputs to gain the average.


print(f"The average of user inputs (excluding -1) is {num_average}.")
