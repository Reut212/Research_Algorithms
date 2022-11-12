import re
from time import sleep

regex = r'^[a-z0-9]+[\._-]?[a-z0-9]+[@][a-z0-9]+[\._-]?[a-z0-9]+[.]\w{2,}$'
validEmails = []
invalidEmails = []


def open_a_text_file(txtFileName):
    # txtFileName = input("Please enter a txt file name: ")
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
