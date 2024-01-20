import socket

# create a socket and connect to a server
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# You've probably noticed that the client doesn't call bind and accept. 
# The client doesn't need to call bind because the client doesn't care about the 
# local IP address and the local port number. 
# The TCP/IP stack within the kernel automatically assigns the local IP address and 
# the local port when the client calls connect. The local port is called an ephemeral 
# port, i.e. a short-lived port.
sock.connect(('localhost', 8888))

# A port on a server that identifies a well-known service that a client connects to is called 
# a well-known port (for example, 80 for HTTP and 22 for SSH). 
# Fire up your Python shell and make a client connection to the server you run on localhost 
# and see what ephemeral port the kernel assigns to the socket you've created 
# send and receive some data
sock.sendall(b'test')

# Another important concept to know is that of a file descriptor. 
# So what is a file descriptor? A file descriptor is a non-negative 
# integer that the kernel returns to a process when it opens an existing file, 
# creates a new file or when it creates a new socket. 
# You've probably heard that in UNIX everything is a file. 
# The kernel refers to the open files of a process by a file descriptor. 
# When you need to read or write a file you identify it with the file descriptor. 
# Python gives you high-level objects to deal with files (and sockets) 
# and you don't have to use file descriptors directly to identify a file but, 
# under the hood, that's how files and sockets are identified in UNIX: 
# by their integer file descriptors.
data = sock.recv(1024)
print(data.decode())
 