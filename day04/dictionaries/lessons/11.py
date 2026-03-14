#!/usr/bin/env python3

contacts = {
    'Jason': {
        'phone': '555-0123',
        'email': 'jason@example.com'
    },
    'Carl': {
        'phone': '555-0987',
        'email': 'carl@example.com'
    },
    "Tony": {
        'phone': '555-0000',
        'email': 'tony@example.com'
    }
}

for contact in contacts:
    print("{}'s contact info:".format(contact))
    print(contacts[contact]['phone'])
    print(contacts[contact]['email'])
