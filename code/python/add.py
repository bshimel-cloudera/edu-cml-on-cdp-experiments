import sys
import cdsw

args = len(sys.argv) - 1  
sum = 0
x = 1

while (args >= x): 
    print ("Argument %i: %s" % (x, sys.argv[x]))
    sum = sum + int(sys.argv[x])
    x = x + 1
    
output_file = open("result.txt", "w")
output_file.write("Sum: " + str(sum))
output_file.close()

print ("Sum of the numbers is: %i." % sum)
