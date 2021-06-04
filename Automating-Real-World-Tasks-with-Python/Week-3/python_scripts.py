########################################
# Introduction to Python Email Library #
########################################

# We'll start by using the email.message.EmailMessage class to create an empty email message.
from email.message import EmailMessage
message = EmailMessage()
print(message)

"""
As usual, printing the message object gives us the string representation of that object. 
The email library has a function that converts the complex EmailMessage object into something 
that is fairly human-readable. Since this is an empty message, there isn't anything to see yet. 
Let's try adding the sender and recipient to the message and see how that looks.

We'll define a couple of variables so that we can reuse them later.
"""
sender = "me@example.com"
recipient = "you@example.com"

# And now, add them to the From and To fields of the message.
message['From'] = sender
message['To'] = recipient
print(message)

# Cool! That's starting to look a bit more like an email message now. How about a subject?
message['Subject'] = 'Greetings from {} to {}!'.format(sender, recipient)
print(message)

"""
From, To, and Subject are examples of email header fields. They’re key-value pairs of labels 
and instructions used by email clients and servers to route and display the email. 
They’re separate from the email's message body, which is the main content of the message.

Let's go ahead and add a message body!
"""
body = """Hey there!

    I'm learning to send emails using Python!"""
message.set_content(body)
