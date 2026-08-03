# Grade Check
name = input("Please enter your Name: ")
score = int(input("Please enter your Score: "))
print()
print("Hello " + name)
print()

if score >= 90:
	print("Grade A")
elif score >= 80:
	print("Grade B")
elif score >= 70:
	print("Grade C")
else:
	print("Grade D")
print()


# Eligibilty Check
name = input("Please enter your Name: ")
age = int(input("Please enter your Age: "))
language = input("Please enter your Favourite Programming Language: ")

if age >= 18 and language == "Python":
	print("Congratulations "+ name + "!")
	print("You are eligible for the AI Engineer Program.")
else:
	print("Sorry " + name)
	print("You are currently not Eligible")