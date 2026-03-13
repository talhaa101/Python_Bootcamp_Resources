#!/usr/bin/env python3

def say_hi():
    print('Hi!')

def say_hi(name):
    print('Hi {}!'.format(name))

def say_hi(name , age):
    print('Hi {}! You are {} years old.'.format(name, age))


say_hi()
#say_hi("tom")
#say_hi("alice", 20)
