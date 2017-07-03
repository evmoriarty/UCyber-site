file_obj = open("rosalind_ini4.txt", "r")

a = input()
b = input()

tot = 0             #Initialize total to 0

if a > b:           #Checks if a > b
    print 'a cannot be greater than b'
elif b > 10000:     #Checks if b > 10000
    print 'b cannot be greater than 10000'
else:               #If neither, then add up odd ints
    for i in range (a,b):
        if i % 2 == 1:
            tot = tot + i

print tot       #Prints the total of odd ints
