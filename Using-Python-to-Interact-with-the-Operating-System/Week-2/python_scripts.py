# Google-IT-Automation-with-Python | Using Python to Interact with the Operating System | Week-2 | Python Scripts

#########################
# Reading Files         #
#########################

# Here we've used the readline method. It lets us read a single line of a file. 
file = open("spider.txt")
print(file.readline())

# We can also call the read method, which reads from the current position until the end of the file instead of just one line.
print(file.read())

# Finally, we close the file using the close method. This open-use-close pattern is a typical way of working with files in most programming languages.
file.close()

# The "with" keyword lets us create a block of code with the work we'd want to do with the file inside of it. 

with open("spider.txt") as file:
  print(file.readline())
