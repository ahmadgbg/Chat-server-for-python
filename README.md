# Chat-server-for-python

This is a python project that allows user chat in one chatroom togheter by connecting to a main chat server.

# How to use

Add the server ip address in client.py and then run.
```
# ADD YOUR SERVER IP BELOW
SERVER = ""
```
To be able to connected outside a local network, port forwarding is a must to the specific port.   
Port can be changed if wanted.

# How to run

Run the application by command line. Use the following command:

###For server
```
python server.py
```

###For client
```
python client.py
```

#How to run without command line
To run the application without command line, then you need to install PyInstaller and compile the application after you have changed ip address for the client.  
You can do this by following these steps:  

1. Install PyInstaller in command line (requires python/pip to be installed):
```
pip install pyinstaller
```
2. Create executable file for client
```
pyinstaller --onefile --noconsole client.py
```
3. Run the created file.