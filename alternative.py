#This program reads in a string. 
#It then manipulates the formatting of the characters and words in order to alternate between cases.
#It uses a combination of for loops and if/elif loops to perform these functions. 
#String manipulation methods such as str(), indexing, split and join are also used.
#The condition of alternate vs other is tested via i % 2 == 0 (with reference to index no.).

user_input = input("Please enter a sentence. ") #reads in a string from the user

#Makes each alternate character into an upper case character and each other into a lower case one.
experiment = "" #final string which takes in the various manipulations
for i in range(len(user_input)): #loops through the string character indices
    if i % 2 == 0: #test for the alternate(the second item)
        experiment = str(experiment) + str(user_input[i]).upper()
    elif i % 2 != 0: 
        experiment = str(experiment) + str(user_input[i]).lower()
        

print(str(experiment)) #combines the manipulated elements together

#Makes each alternate word lower case and each other upper case
split_1 = user_input.split() #creates a list of words from the input string

print(split_1) #checks the list

experiment_2 = ""#final string which takes in the various manipulations

for x in range(len(split_1)): #loops through the word amount
    if x % 2 == 0: #test for the alternate(the second item)
        experiment_2 = str(experiment_2) + str(split_1[x]).lower()
    elif x % 2 != 0: 
        experiment_2 = str(experiment_2) + str(split_1[x]).upper()
        
        
print("".join(experiment_2))#combines the manipulated elements together
