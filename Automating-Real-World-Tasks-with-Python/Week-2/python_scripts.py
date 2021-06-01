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
