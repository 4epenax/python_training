from model.group import Group
import random
import string

constant = [
    Group(name="name1", header="header1", footer="footer1"),
    Group(name="name2", header="header2", footer="footer2")
]


def random_string(prefix, maxlen):
    symbol = string.ascii_letters + string.digits + " " * 10
    return prefix + "".join([random.choice(symbol) for i in range(random.randrange(maxlen))])


testdata = [
    Group(name=name, header=header, footer=footer)
    for name in ["", random_string("N", 10)]
    for header in ["", random_string("H", 20)]
    for footer in ["", random_string("F", 20)]
]

testdatagen = [Group(name="", header="", footer="")] + [
    Group(name=random_string("n", 10), header=random_string("h", 20),
          footer=random_string("f", 20))
    for i in range(4)
]
