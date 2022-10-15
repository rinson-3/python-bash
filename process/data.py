def to_seconds(hours,minutes,seconds):
    return hours*3600+minutes*60+seconds

print("Wecome to the  time converter")

conti="y"
while (conti.lower()=="y"):
    hours=int(input("Enter the hours:"))
    minutes=int(input("Enter the minutes:"))
    seconds=int(input("Enter the seconds:"))
    print(f"Total seconds = {to_seconds(hours,minutes,seconds)}")
    conti=input("Do you want to continue? [y to continue]")

print("Good Bye!")

# to acces environment variables
# use "export"("set"- for windows) command to set environment variables

import os
print("HOME: " + os.environ.get("HOME",""))
print("SHELL: " + os.environ.get("SHELL",""))
print("FRUIT: " + os.environ.get("FRUIT",""))


# access values from command line

import sys
print(sys.argv)
# $? is used to see the exit status from the linux terminal, it prints 1 if any command fails and 0 if command succeeds.


# sys.argv helps to access command line arguments from cmd/shell to python
import os
import sys
filename=sys.argv[1]

if not os.path.exists(filename):
    with open(filename, "w") as f:
        f.write("New file created")

else:
    print(f"Error {filename} already exits")
    sys.exit(1)



    