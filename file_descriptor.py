# As I mentioned before, even though Python gives you a high-level file or 
# file-like object to work with, you can always use the fileno() method on 
# the object to get the file descriptor associated with the file.

import sys
import os

print(sys.stdin.fileno())
print(sys.stdout.fileno())
print(sys.stderr.fileno())

os.write(sys.stdout.fileno(), b'hello\n')

# And here is an interesting part - which should not be surprising to you anymore because
# you already know that everything is a file in Unix - your socket also has a 
# file descriptor associated with it. Again, when you create a socket in 
# Python you get back an object and not a non-negative integer, but you can always 
# get direct access to the integer file descriptor of the socket with the fileno() 
# method that I mentioned earlier.

import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(sock.fileno())