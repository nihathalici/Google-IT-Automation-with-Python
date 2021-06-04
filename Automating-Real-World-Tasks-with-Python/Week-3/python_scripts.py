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

########################
# Adding Attachments   #
########################

"""
In order for the recipient of your message to understand what to do with an attachment, 
you  need to label the attachment with a MIME type and subtype to tell them what sort of file you’re sending. 
The Internet Assigned Numbers Authority (IANA) (iana.org) hosts a registry of valid MIME types. 
If you know the correct type and subtype of the files you’ll be sending, you can use those values directly. 
If you don't know, you can use the Python mimetypes module to make a good guess!
"""
import os.path
attachment_path = '/tmp/example.png'
attachment_filename = os.path.basename(attachment_path)
import mimetypes
mime_type, _ = mimetypes.guess_type(attachment_path)
print(mime_type)

"""
Alright, that mime_type string contains the MIME type and subtype, separated by a slash. 
The EmailMessage type needs a MIME type and subtypes as separate strings, so let's split this up:
"""
mime_type, mime_subtype = mime_type.split('/', 1)
print(mime_type)
print(mime_subtype)

# Now, finally! Let's add the attachment to our message and see what it looks like.
with open(attachment_path, 'rb') as ap:
    message.add_attachment(ap.read(),
                           maintype=mime_type,
                           subtype=mime_subtype,
                           filename=os.path.basename(attachment_path))
print(message)

"""
The entire message can still be serialized as a text string, including the image that we attached! 
The email message as a whole has the MIME type "multipart/mixed". 
Each part of the message has its own MIME type. The message body is still there as a "text/plain" part, 
and the image attachment is a "image/png" part. 
"""
