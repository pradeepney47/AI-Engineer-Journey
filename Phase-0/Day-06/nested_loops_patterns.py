# Nested loops and pattern problems

# Pattern 1: Print increasing number of stars
# i is in the range of 4 so the sequence is 0 1 2 3
# j is in the range of i + 1
print () 
print ("Increasing number of stars")
print ()
for i in range (4):
    for j in range (i + 1):
        print ("*", end="")
    print ()
print ()

# Pattern 2: Print decreasing number of stars
# i is in the range of 4 so the sequence is 0 1 2 3
# j is in the range of 4 - i
print () 
print ("Decreasing number of stars")
print ()
for i in range (4):
    for j in range (4 - i):
        print ("*", end="")
    print ()
print ()

# Pattern 3: Print increasing number of stars with decreasing spaces
# i is in the range of 4 so the sequence is 0 1 2 3
# j is in the range of 3 - i
# k is in the range of i + 1
print () 
print ("Increasing number of stars with decreasing spaces")
print ()
for i in range (4):
    for j in range (3 - i):
        print (" ", end="")
    for k in range (i + 1):
        print ("*", end="")
    print ()
print ()


# Pattern 4: Print increasing odd number of stars
# i is in the range of 4 so the sequence is 0 1 2 3
# j is in the range of 2 * i + 1
print () 
print ("Increasing odd number of stars")
print ()
for i in range (4):
    for j in range (2 * i + 1):
        print ("*", end="")
    print ()
print ()

# Pattern 5: Print decreasing odd number of stars
# i is in the range of 4 so the sequence is 0 1 2 3
# j is in the range of -2 * i + 7
print () 
print ("Decreasing odd number of stars")
print ()
for i in range (4):
    for j in range (-2 * i + 7):
        print ("*", end="")
    print ()
print ()