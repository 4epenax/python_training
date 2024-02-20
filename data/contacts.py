# -*- coding: utf-8 -*-
from model.contact import Contact

testdata = [
    Contact(firstname="fn", middlename="mn", lastname="ln", nickname="nn", title="t1", company="c2",
            address="a3", homephone="hp", mobilephone="mp", workphone="wp", fax="f4", email="el",
            email2="el2", email3="el3", homepage="hp4", bday="13", bmonth="May", byear="1968",
            aday="4", amonth="April", ayear="2020"),
    Contact(firstname="fnt", middlename="mnt", lastname="lnt", nickname="nnt", title="t1t",
            company="c2t", address="a3t", homephone="hpt", mobilephone="mpt", workphone="wpt",
            fax="f4t", email="elt", email2="el2t", email3="el3t", homepage="hp4t", bday="11",
            bmonth="April", byear="1977", aday="7", amonth="May", ayear="2016")
]
