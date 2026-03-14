#!/usr/bin/env python3

contacts = {
    'Jason': ['555-0123', '555-0000' , '555-1111'],
    'Carl': ['555-0987']
}

for number in contacts['Carl']:
    print('Phone: {}'.format(number))
