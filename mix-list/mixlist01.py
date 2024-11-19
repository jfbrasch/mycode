#!/usr/bin/env python3

## Python Basics  - Working with Lists lab 16

# Creating a list

my_list = [ "192.168.0.5", 5060, "UP" ]

# excerise in printing items from list.

print("The first item in the list (IP): " + my_list[0] )
print("The second item in the list (port): " + str(my_list[1]) )
print("The last item in the list (state): " + my_list[2] )

# CHALLENGE 01 -  Given a list, display only the IP addresses on the screen.

iplist = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]


print("List of IP addresses: " + iplist[3] + ", " + iplist[4])

