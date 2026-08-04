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





















