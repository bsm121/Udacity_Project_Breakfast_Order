import time

#first we make our functions that will be used more than once inside other functions. This one is for print and time.sleep.
def print_pause (message_printed):
    print(message_printed)
    time.sleep(2)

#next is to make sure the user imputs valid input. There will be 3 parameters, the prompt, and two options. There could also be a list here.

def valid_input (prompt, input1, input2):
    #start with a while loop that continues until user gives good input.
    while True:
        #the variable is set to "response", this is what the user types in, and will accept upper and lower-case letters.
        response = input(prompt).lower()
        #here we make if/elif/else statements to check for valid input.
        if input1 in response:
            break # this means option1 was found and the input is valid and the program breaks out of the inner loop and returns response
        elif input2 in response:
            break #ends program if option2 is found and breaks out of inner loop and returns response
        else:
            print_pause("I'm sorry I don't understand.")

    return response # we now have the user input as the variable response and have validated it.

# Now we start the primary functions. We start with the introduction that is timed for 2 seconds each.
def intro ():
    print_pause("Hello I am Bob, the Breakfast Bot.")
    print_pause("Today we have two breakfasts available.")
    print_pause("The first is waffles with whipped cream and maple syrup.")
    print_pause("The second is sweet potato pancakes with butter and maple syrup.")

def get_order ():
    #first we will run the valid_input function from above with 3 parameters.
    #response is the variable set to run the valid_input function.
    response = valid_input("Please place your order. " "Would you like waffles or pancakes?\n", "waffles", "pancakes")
    # if statement checks if order is waffles, if true then prints nice statement and says order ready soon.
    if "waffles" in response:
        print_pause("waffles it is!")
    # elif statement checks if order is waffles, if true then prints nice statement and says order ready soon.
    elif "pancakes" in response:
        print_pause("pancakes it is!")
    print_pause("Your order will be ready shortly.")

#we ask if they want anything else. 
#we use the valid_input function again but with different parameters to check by the internal function.
def order_again():
    response = valid_input("Would you like to place another order? " "Please say yes or no.\n", "yes", "no")
    if "no" in response:
        print_pause("Ok, goodbye!") # this will end the function.
    if "yes" in response:
        print_pause("Very good, I'm ready to take another order.")
        get_order() #this will call the get_order() function again, it only runs inside the "yes loop".

#Now we just create another function to call the other functions.
def order_breakfast():
    intro() #intro called and executed
    get_order() #get_order called and executed
    order_again() #order_again called and executed

#This will call the order breakfast function.
order_breakfast()






      