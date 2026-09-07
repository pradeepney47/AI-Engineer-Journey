# print 1 to 10 in while loop
number = 1
while number <= 9:
    print(number)
    number = number + 1
print(number)

# countdown
message = "Blast Off!"
count = 5
while count >= 1:
    print(count)
    count = count - 1
print(message)

# password retry
correct_password = "Python123"

password_typed = "" # initial state of the variable

while password_typed != correct_password: # condition

    # change of state of the variable
    password_typed = input("Please enter your password: ") 

    if password_typed != correct_password:
        print("Wrong Password. Try Again.")
        
print("Access Granted.")


# Break free from Infinite Samsaric Pattern
def samsara(movement):
    #if there is a self movement
    if movement: 
        #to defend one's self (via affect, cognition, and behaviour as one consciousness)
        ego = 1
        #self is empty (because there is no permanent self)
        self = []
        #while defending oneself is always trapped within consciousness pattern
        while ego >= 0:
            #consciousness being a source
            if movement[ego] == "yang": 
                #self is always experienced as presence
                self += ["presence"]
            #consciousness being a shadow
            elif movement[ego] == "yin": 
                #self is always experienced as absence
                self += ["absence"]
            #but by down regulating the defensive ego we can break away from this infinite loop
            ego -= 1
        #and can return to see the actual movement of self    
        return self
    else:
        #self is empty but not it's movement
        raise ValueError("Movement of self can never be empty!") 
#duality in movement (only constant is movement of source and shadow)
movement = ["yin", "yang"]
# movement = []
try:
    #when we try to see the movement being passed inside samsaric function, 
    #actual nirvana is attained
    nirvana = samsara(movement)
except ValueError as move_self_never_empty:
    print()
    #movement of self can never be empty (although self is empty)
    print(move_self_never_empty) 
else:
    #nirvana is to break away from samsaric patterns by understanding the movement of self is non-dual
    #and it is the co-existence of presence and absence
    print()
    print("Self is a movement of " + " and ".join(nirvana), "!")
    print()





