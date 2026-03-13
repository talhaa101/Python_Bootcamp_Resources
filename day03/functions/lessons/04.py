#!/usr/bin/env python3

# built in functions: print(), input(), len(), format() etc.
# user defined functions: say_hi()

'''
def say_hi(name):
    print('Hi {}!'.format(name))
'''

'''
def say_hi(name):
    print(f'Hi {name}!')  # this is a new way to format strings, called f-strings
'''

def say_hi(name):
   print( "Hi " + str(name) + " !" )  # this is the old way to format strings, using concatenation  # str(5) = '5'  
say_hi('Jason')
say_hi('everybody')
say_hi(5.0)  # this is not a good idea, but it works because of the way format() works
