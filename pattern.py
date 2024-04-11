#A code printing out an increasing and then decreasing pattern of stars.
#It uses a nested if-else statement within a for-loop to create the conditions for this pattern.

stars = "*"
stars_neg = "****" #a variable to use for the decreasing countdown.

for i in range(0,10): #the number of lines of output.
    
        if i < 5: #lines up to the decreasing countdown
            print(stars) #displays an increasing pattern of stars
            stars = stars +"*" #allows the output to increase incrementally
        else: 
            index = 10-i #create a decreasing countdown using a negative slice.
            print(stars_neg[0:index]) #display the decreasing pattern of stars
            