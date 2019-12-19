from model.groups import Group
import random
import string
import os
import jsonpickle

def random_string (prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10 #+ string.punctuation
    return prefix + "".join([random.choice(symbols) for i in range (random.randrange(maxlen))])

testdata = [Group(name ='', header ='', footer ='')] + [
    Group(name = random_string("name",10), header = random_string("header",20), footer = random_string("footer",20))
    for x in range(5)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../data/groups.json')

with open (file, "w") as f:
    jsonpickle.set_encoder_options("json", indent = 2)
    f.write(jsonpickle.dumps(testdata))