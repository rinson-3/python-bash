file=open("spider.txt",encoding="utf8")    # Here using "open" we can use this object in multiple places
print(file.readline())
print(file.read())

file.close() # close the file or use the with command


with open("spider.txt") as file:  # use the file in 1 block
    print(file.readline())


# iterating through the file

with open("spider.txt") as file:   # creates empty lines in between text, use strip method
    for line in file:
        print(line.upper())


with open("spider.txt") as file:
    for line in file:
        print(line.strip().upper())



# write to a file

with open("spider.txt", "w") as file: # writing files will remove the previous content from the file
    file.write("dark and stormy night")
    