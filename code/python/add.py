import sys
import cdsw

args = len(sys.argv) - 1  
sum = 0
x = 1

while (args >= x): 
    print ("Argument %i: %s" % (x, sys.argv[x]))
    sum = sum + int(sys.argv[x])
    x = x + 1
    
with open("result.txt", "w") as output_file:
    output_file.write(f"Input: {sys.argv[1:]},")
    output_file.write(f"Sum: {sum}")
    output_file.close()

cdsw.track_metric("Count", args)
cdsw.track_metric("Sum", sum)

cdsw.track_file("result.txt")

print ("Sum of the numbers is: %i." % sum)