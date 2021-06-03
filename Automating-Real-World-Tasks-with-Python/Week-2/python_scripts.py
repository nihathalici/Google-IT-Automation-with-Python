#########################
# Data Serialization    #
#########################

"""
Instead of having a list of lists, we could turn this information into a list of dictionaries. 
In each of these dictionaries, the key will be the name of the column, and the value will be the corresponding information in each row.  
It could look something like this:  
"""
people = [
    {
        "name": "Sabrina Green",
        "username": "sgreen",
        "phone": "802-867-5309",
        "department": "IT Infrastructure",
        "role": "Systems Administrator"
    },
    {
        "name": "Eli Jones",
        "username": "ejones",
        "phone": "684-348-1127",
        "department": "IT Infrastructure",
        "role": "IT Specialist"
    },
]

"""
Using a structure like this lets us do interesting things with our information that’s much harder to do with CSV files. 
For example, let's say we want to record more than one phone number for each person. 
Instead of using a single string for "phone", we could represent that data in another dictionary, like this: 
"""
people = [
    {
        "name": "Sabrina Green",
        "username": "sgreen",
        "phone": {
            "office": "802-867-5309",
            "cell": "802-867-5310"
        },
        "department": "IT Infrastructure",
        "role": "Systems Administrator"
    },
    {
        "name": "Eli Jones",
        "username": "ejones",
        "phone": {
            "office": "684-348-1127"
        },
        "department": "IT Infrastructure",
        "role": "IT Specialist"
    },
]

"""
Now, we can record multiple phone numbers per person, and give them descriptive names like "office" and "cell". 
This would be hard to store in a CSV file, because the data is not flat. 
To help us with that, there's a bunch of different formats that we can use to store our data when the structure isn't flat.
"""

#################################
# Data Serialization Formats    #
#################################


"""
JSON (JavaScript Object Notation) is the serialization format that we'll use the most in this course. 
We'll go into some details later but, for now, let's just use the json module to convert our people list of dictionaries into JSON format.  
"""

import json

with open('people.json', 'w') as people_json:
    json.dump(people, people_json, indent=2)

# This code uses the json.dump() function to serialize the people object into a JSON file. 

"""
YAML (Yet Another Markup Language) has a lot in common with JSON. They’re both formats that can be easily understood by a human 
when looking at the contents. In this example, we’re using the yaml.safe_dump() method to serialize our object into YAML: 
"""
import yaml

with open('people.yaml', 'w') as people_yaml:
    yaml.safe_dump(people, people_yaml)

#################################
# More About JSON               #
#################################

"""
The json library will help us turn Python objects into JSON, and turn JSON strings into Python objects! 
The dump() method serializes basic Python objects, writing them to a file. Like in this example:  
"""
import json
with open('people.json', 'w') as people_json:
    json.dump(people, people_json)
 
"""
JSON doesn't need to contain multiple lines, but it sure can be hard to read the result if it's formatted this way! 
Let's use the indent parameter for json.dump() to make it a bit easier to read.  
"""
with open('people.json', 'w') as people_json:
    json.dump(people, people_json, indent=2)

    
# Another option is to use the dumps() method, which also serializes Python objects, but returns a string instead of writing directly to a file.  
people_json = json.dumps(people)

"""
The load() method does the inverse of the dump() method. It deserializes JSON from a file into basic Python objects. 
The loads() method also deserializes JSON into basic Python objects, but parses a string instead of a file.  
"""
with open('people.json', 'r') as people_json:
    people = json.load(people_json)

    
#################################
# The Python Requests Library   #
#################################

"""
The Python Requests library makes it super easy to write programs that send and receive HTTP. 
Instead of having to understand the HTTP protocol in great detail, you can just make very simple HTTP connections 
using Python objects, and then send and receive messages using the methods of those objects.
"""
import requests
response = requests.get('https://www.google.com')

# Alright, now what did the web server respond with? Let's take a look at the first 300 characters of the Response.text:
print(response.text[:300])

"""
We didn't have to write any code to find the web server, make a network connection, construct an HTTP message, 
wait for a response, or decode the response. Not that HTML can't be messy enough on its own, 
but let's look at the first bytes of the raw message that we received from the server:
"""
response = requests.get('https://www.google.com', stream=True)
print(response.raw.read()[:100])

"""
The requests.Response object also contains the exact request that was created for us. 
We can check out the headers stored in our object to see that the Requests module told the web server that it was okay to compress the content: 
"""
response.request.headers['Accept-Encoding']

# And then the server told us that the content had actually been compressed.  
response.headers['Content-Encoding']

###########################################
# Useful Operations for Python Requests   #
###########################################

"""
How do we know if a request we made got a successful response? 
You can check out the value of Response.ok, which will be True if the response was good, and False if it wasn't.  
"""
response.ok

# If the boolean isn’t specific enough for your needs, you can get the HTTP response code that was returned by looking at Response.status_code:  
response.status_code

"""
To write maintainable, stable code, you’ll always want to check your responses to make sure they succeeded 
before trying to process them further. For example, you could do something like this:  
"""
response = requests.get(url)
if not response.ok:
    raise Exception("GET failed with status code {}".format(response.status_code))
    
"""
But you don't really need to do that. Requests has us covered here, too! 
We can use the Response.raise_for_status() method, which will raise an HTTPError exception only if the response wasn’t successful.  
"""
response = requests.get(url)
response.raise_for_status()

###############################
# HTTP GET and POST Methods   #
###############################

# With requests.get(), you can provide a dictionary of parameters, and the Requests module will construct the correct URL for you!  
import requests
p = {"search": "grey kitten","max_results": 15}
response = requests.get("https://example.com/path/to/api", params=p)
response.request.url

"""
A POST request looks very similar to a GET request. Instead of setting the params attribute, 
which gets turned into a query string and appended to the URL, we use the data attribute, 
which contains the data that will be sent as part of the POST request. 
"""
p = {"description":"white kitten", "name":"Snowball", "age_months": 6}
response = requests.post("https://example.com/path/to/api", data=p)

"""
So, if we need to send and receive data from a web service, we can turn our data 
into dictionaries and then pass that as the data attribute of a POST request.

Today, it's super common to send and receive data specifically in JSON format, 
so the Requests module can do the conversion directly for us, using the json parameter.
"""
response = requests.post("https://example.com/path/to/api", json=p)
response.request.url
response.request.body
