# While loops are used to execute a block of code repeatedly as long as a certain condition is true.
# The syntax for a while loop is as follows:

it = 4
while it > 0:
    print("The value of it is: " + str(it))
    it -= 1  # This is equivalent to it = it - 1
print ("While loop completed successfully")

iz  = 10
while iz > 0:
    if iz % 2 == 0:
        print("Print the even number: "  +str(iz))
    iz -= 1
    print("*******************************************")
    if iz !=3 and iz != 5:
        print("Skipp Printing 3 and 5: " + str(iz))
        iz -= 1
print ("While loop completed successfully")

xy = 10
while xy > 1:
   if xy == 3:
       break
   print("Breaking the loop when xy is: " + str(xy))
   xy = xy-1

z = 10
while z > 1:
    if z == 9:
        z = z - 1
        continue
    print("Skipping the value when z is: " + str(z))
    if xy == 3:
        break
    print("Breaking the loop when xy is: " + str(xy))
    xy = xy - 1
