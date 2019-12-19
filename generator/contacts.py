import os
from model.contact import Contact
import jsonpickle
import random
import string
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = 'data/contacts.json'

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10 #+ string.punctuation
    return prefix + "".join(random.choice(symbols) for x in range(random.randrange(maxlen)))

testdata = [Contact(firstname = "", middlename = "", lastname = "", nickname = "", homephone = "", mobilephone = "", workphone = "", secondaryphone = "", address = "", title = "",
                    company = "", email ="" , email2 ="", email3 = "")] + [
    Contact(
        firstname = random_string("firstname", 15), middlename = random_string("middlename", 15), lastname = random_string("lastname", 15), nickname = random_string("nickname", 5),
        homephone = random_string("homephone", 10), mobilephone = random_string("mobilephone", 10), workphone = random_string("workphone", 10), secondaryphone = random_string("secondaryphone", 10),
        address = random_string("address", 15), title = random_string("title", 5), company = random_string("company", 10), email = random_string("email", 10), email2 = random_string("email2", 10),
        email3 = random_string("email3", 10)
    )
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as f:
    jsonpickle.set_encoder_options("json", indent = 2)
    f.write(jsonpickle.dumps(testdata))