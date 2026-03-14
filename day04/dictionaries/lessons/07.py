#!/usr/bin/env python3

contacts = {
    'Jason': ['555-0123', '555-0000'],
    'Carl': '555-0987'
}

if 'Jason' in contacts.keys():
    print("Jason's phone number is:")
    print(contacts['Jason'][1])

if 'Carl' in contacts.keys():
    print("Carl's phone number is:")
    print(contacts['Carl'])