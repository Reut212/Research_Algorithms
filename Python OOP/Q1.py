import os
import re
from time import sleep

"""
This is an implementation for valid email addresses search.

The program supplies two function, open_a_text_file(txtFileName) and check(email). For example, 
>>> open_a_text_file("txt.txt")
Valid Emails are:  ['abc-d@mail.com', 'abc.def@mail.com', 'abc@mail.com', 
'abc_def@mail.com', 'abc.def@mail.cc', 'abc.def@mail-archive.com', 'abc.def@mail.org', 'abc.def@mail.com'] Invalid 
Emails are:  ['abc-@mail.com', 'abc..def@mail.com', '.abc@mail.com', 'abc#def@mail.com', 'abc.def@mail.c', 
'abc.def@mail#archive.com', 'abc.def@mail', 'abc.def@mail..com'] 
"""

regex = r'^[a-z0-9]+[\._-]?[a-z0-9]+[@][a-z0-9]+[\._-]?[a-z0-9]+[.]\w{2,}$'
validEmails = []
invalidEmails = []


def open_a_text_file(txtFileName):
    """
    Receive txt file name from user and looking for a valid and invalid email addresses according to known pattern (
    regex).
    There is an implementation for inserting a txt file and this function also check if the received file is a txt file.
    I marked it as notes.
    """

    # txtFileName = input("Please enter a txt file name: ")
    ext = os.path.splitext(txtFileName)[-1].lower()
    if ext != '.txt':
        print(ext, "is an unknown file format.")
        return
    # print()
    # print("looking for " + str(txtFileName) + "...")
    # print()
    # sleep(0.5)

    try:
        with open(txtFileName) as tf:
            while True:
                emailAddress = tf.readline()
                if emailAddress.endswith('\n'):
                    emailAddress = emailAddress[:-1]
                check(emailAddress)
                if not emailAddress:
                    break
        print("Valid Emails are: ", validEmails)
        print("Invalid Emails are: ", invalidEmails[:-1])
    except FileNotFoundError:
        print("There is no txt file exist under this name. ")


def check(email):
    """
    recieve email address and add it to invalid / valid lists
    For example,
    >>> check('abc-d@mail.com')
    Valid Emails: ['abc-@mail.com']
    >>> check('abc-d@mail.com')
    Invalid Emails are:  ['abc-@mail.com']
    """

    if email == '/0':
        return
    if re.match(regex, email):
        validEmails.append(email)
        # print("Valid Email: " + str(email))
    else:
        invalidEmails.append(email)
        # print("Invalid Email " + str(email))


if __name__ == '__main__':
    open_a_text_file("txt.txt")
    # open_a_text_file()
