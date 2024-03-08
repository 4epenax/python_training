from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 8
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbol = string.ascii_letters + string.digits + " " * 10
    return prefix + "".join([random.choice(symbol) for i in range(random.randrange(maxlen))])


testdata = [
    Contact(firstname=random_string("fn", 10), middlename=random_string("mn", 10),
            lastname=random_string("ln", 10), nickname=random_string("nn", 10),
            title=random_string("t1", 10), company=random_string("c2", 10),
            address=random_string("a3", 10), homephone=random_string("hp", 10),
            mobilephone=random_string("mp", 10), workphone=random_string("wp", 10),
            fax=random_string("f4", 10), email=random_string("el", 10),
            email2=random_string("el2", 10), email3=random_string("el3", 10),
            homepage=random_string("hp4", 10), bday="13", bmonth="May", byear="1968", aday="4",
            amonth="April", ayear="2020")
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
