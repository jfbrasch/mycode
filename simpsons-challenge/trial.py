#!/usr/bin/env python3

## Lab72, the Simpsons Slicing Challenge!

# Given the following lists.  print - My eyes! The goggles do nothing!

challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]


trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]


nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]


# Challenge - 
# print("My " + challenge[2][1] + "! The " + challenge[2][0] + " do " + challenge[3] + "!")

# Trial -
print("My " + trial[2]['goggles'] + "! The " + trial[2]['eyes'] + " do " + trial[3] + "!")

