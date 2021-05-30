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

############################
# Iterating through Files  #
############################

# File objects can be iterated in the same way as other Python sequences like list or strings.
# We can use a string method, strip to remove all surrounding white space, including tabs and new lines.
with open("spider.txt") as file:
    for line in file:
        print(line.strip().upper())
        
# The lines have been sorted alphabetically, so they're no longer in the order that they were in the file. 
file = open("spider.txt")
lines = file.readlines()
file.close()
lines.sort()

#########################
# Writing Files         #
#########################

# Using the write method on a file object writes contents to it instead of reading from it.
with open("novel.txt") as file:
    file.write("I was ...")
#########################
# Practice              #
#########################

'''
In this exercise, we will test your knowledge of reading and writing files by playing around with some text files.

Let's say we have a text file containing current visitors at a hotel. 
We'll call it, guests.txt. Run the following code to create the file. 
The file will automatically populate with each initial guest's first name on its own line.
'''

guests = open("guests.txt", "w")
initial_guests = ["Bob", "Andrea", "Manuel", "Polly", "Khalid"]

for i in initial_guests:
    guests.write(i + "\n")
    
guests.close()

# No output is generated for the above code cell. To check the contents of the newly created guests.txt file, run the following code.
with open("guests.txt") as guests:
    for line in guests:
        print(line)
        
'''
The output shows that our guests.txt file is correctly populated with each initial guest's first name on its own line. Cool!
Now suppose we want to update our file as guests check in and out. 
Fill in the missing code in the following cell to add guests to the guests.txt file as they check in.
'''
new_guests = ["Sam", "Danielle", "Jacob"]

with open("guests.txt", 'a') as guests:
    for i in new_guests:
        guests.write(i + "\n")

guests.close()

# To check whether your code correctly added the new guests to the guests.txt file, run the following cell.
with open("guests.txt") as guests:
    for line in guests:
        print(line)
'''
The current names in the guests.txt file should be: Bob, Andrea, Manuel, Polly, Khalid, Sam, Danielle and Jacob.
Was the guests.txt file correctly appended with the new guests? If not, go back and edit your code making sure to fill in the gaps appropriately so that the new guests are correctly added to the guests.txt file. Once the new guests are successfully added, you have filled in the missing code correctly. Great!
Now let's remove the guests that have checked out already. There are several ways to do this, however, the method we will choose for this exercise is outlined as follows:
Open the file in "read" mode.
Iterate over each line in the file and put each guest's name into a Python list.
Open the file once again in "write" mode.
Add each guest's name in the Python list to the file one by one.
Ready? Fill in the missing code in the following cell to remove the guests that have checked out already.
'''
checked_out=["Andrea", "Manuel", "Khalid"]
temp_list=[]

with open("guests.txt", 'r') as guests:
    for g in guests:
        temp_list.append(g.strip())

with open("guests.txt", 'w') as guests:
    for name in temp_list:
        if name not in checked_out:
            guests.write(name + "\n")
        
# To check whether your code correctly removed the checked out guests from the guests.txt file, run the following cell.
with open("guests.txt") as guests:
    for line in guests:
        print(line)

'''
The current names in the guests.txt file should be: Bob, Polly, Sam, Danielle and Jacob.

Were the names of the checked out guests correctly removed from the guests.txt file? 
If not, go back and edit your code making sure to fill in the gaps appropriately so that the checked out guests are correctly removed from the guests.txt file. 
Once the checked out guests are successfully removed, you have filled in the missing code correctly. Awesome!

Now let's check whether Bob and Andrea are still checked in. How could we do this? We'll just read through each line in the file to see if their name is in there. 
Run the following code to check whether Bob and Andrea are still checked in.
'''
guests_to_check = ['Bob', 'Andrea']
checked_in = []

with open("guests.txt","r") as guests:
    for g in guests:
        checked_in.append(g.strip())
    for check in guests_to_check:
        if check in checked_in:
            print("{} is checked in".format(check))
        else:
            print("{} is not checked in".format(check))

# We can see that Bob is checked in while Andrea is not. Nice work! You've learned the basics of reading and writing files in Python!


############################
# Working with Files       #
############################

'''
We first import the OS module. Then we call the remove function the OS module gives us 
and pass the string novel.txt which is the file we created earlier. The file has now been deleted.
'''
import os
os.remove("novel.txt")


'''
We can easily rename a file with the rename function. The first parameter to rename function 
is the old name of the file and the second is new name. 
'''
os.rename("first_draft.txt", "finished_masterpiece.txt")

# We can use OS path sub-module exists function to check whether a file exist. 
os.path.exists("finished_masterpiece.txt")

############################
# More File Information    #
############################

'''
We can get a lot more info about our files using functions in OS.path module. 
For example, to check how big a file is, we can use the getsize function which returns the file size in bytes.
'''
os.path.getsize("spider.txt")

# To check when the file was last modified, the getmtime function comes in really handy.
os.path.getmtime("spider.txt")


'''
Here, we're using the fromtimestamp method of the datetime class inside the datetime module. 
It makes the date far easier for us to understand.
'''
import datetime
timestamp = os.path.getmtime("spider.txt")
datetime.datetime.fromtimestamp(timestamp)

# The abspath function takes a filename and turns it into an absolute path. 
os.path.abspath("spider.txt")

#########################
# Directories           #
#########################

# To check which current directory your Python program is executing in, you can use the getcwd method.
import os
print(os.getcwd())

# To create a directory, we use the mkdir function.
os.mkdir("new_dir")

# You can also change directories in your program by using the chdir function 
# and passing the directory you'd like to change to as a parameter.
os.chdir("new_dir")

# We can use rmdir to remove a directory
os.rmdir("newer_dir")

# The os.listdir function returns a list of all the files and sub-directories in a given directory.
os.listdir("website")


# If we want to know whether one of these files is a directory, 
# we need to use os.path.join to create the full path.

dir = "my_directory"

for name in os.listdir(dir):
    fullname = os.path.join(dir, name)
    if os.path.isdir(fullname):
        print("{} is a directory".format(fullname))
    else:
        print("{} is a file".format(fullname))

# In Linux and MacOS, the portions of a file are split using a forward slash(/)
# On Windows, they're split using a backslash (\)

#########################
# Reading CSV Files     #
#########################

'''
Python standard library includes a module which lets us read, create and manipulate CSV files: CSV
Before we can parse a CSV file, we need to open the file the same way as before.
That has given us an instance of the CSV reader class. 
We can now iterate through its contents and access information that it parsed.

import csv
f = open("csv_file.txt")
csv_f = csv.reader(f)
for row in csv_f:
    name, phone, role = row
    print("Name: {}, Phone: {}, Role: {}".format(name, phone, role))
f.close()


#########################
# Generating CSV        #
#########################

"""
Open the file in write mode. We'll use the with block that we saw before
Now that we have the file opened for writing, let's call the writer function of the CSV module with this file as a parameter.
The writer variable is now an instance of a CSV writer class. 
There are two functions that we can use: writerow, which we'll write one row at a time; and writerows, which we'll write all of them together.
"""

import csv
hosts = [["workstation.local", "192.168.25.46"], ["webserver.cloud", "10.2.5.6"]]

with open('hosts.csv', 'w') as hosts_csv:
    writer = csv.writer(hosts_csv)
    writer.writerows(hosts)

################################
# Reading and Writing          #
# CSV Files with Dictionaries  #
################################

"""
We can profit from this additional information by using DictReader, a slightly different reader that's also provided by the CSV module. 
This reader turns each row of the data in a CSV file into a dictionary. 
We can then access the data by using the column names instead of the position in the row.
"""
import csv
with open('software.csv') as software:
    reader = csv.DictReader(software)
    for row in reader:
        print(("{} has {} users").format(row["name"], row["users"]))
