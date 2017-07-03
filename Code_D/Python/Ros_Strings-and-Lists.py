s = raw_input()

a = input()
b = input()
c = input()
d = input()

output = ''                 #Initialize Ouput to a blank str

for i in s[a : b+1]:        #Get the str from s[a:b]
    output = output + i

output = output + ' '

for q in s[c : d+1]:        #Get the str from s[c:d]
    output = output + q

print output                #Print the output
