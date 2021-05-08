# Socket-Squares

## Description

Socket-Squares is a simple pygame application that allows users to connect to a server and see eachother move their randomly generated squares around. This application is a means for me to learn and use sockets without following a complete tutorial. I have zero experience with netcode for a "game" up until now, so systems likely have better implementations.

Max Players: 8
## Installation

### Release (for those that just want to play):

1. Download the [latest release](https://github.com/kirigaine/Socket-Squares/releases) for your operating system
2. Extract files in desired directory
3. ***[LINUX]*** Ensure *server* and *client* have permission to execute 
      - *Note: Below is the simplest way to give permission, but consider your own security needs depending on your system/network*
      - ```sudo chmod +x client server```
4. Done!

### Source Files (for those that may want to alter code):

1. Download compressed source files from repository
2. Extract files in desired directory
3. Run ```python``` in a terminal
4. Run ```pip install -r requirements.txt ```in python terminal to install all required packages
5. Done!

## Usage

### Release

1. Run *server* to begin hosting a session if needed, then connect with *client* by entering an IPv4 and hitting enter!
2. ***[WINDOWS]*** When running either executable, Windows Security may pop up a window saying "Windows protected your PC"
   - *Note: There is no security risk in running this program*
   - Bypass this by clicking **"More info"**, then clicking **"Run anyway"**
3. Press 'ESC' key to exit the client at any time.

### Source Files
1. Run server.py on the desired host with python
   - ```python server.py```
2. Clients run client.py with python and enter the IPv4 of the desired server 
   - ```python client.py```
3. Press 'ESC' key to exit the client at any time

## Controls (Client)

W/A/S/D - Move Up/Left/Down/Right

ESC - Exit

## Known Issues

1. The socket has multiple ways to fail connecting over the internet. When hosting, make sure to port forward 26256 TCP for your router, check your firewall, and consider other standard errors when hosting/connecting online.

2. The older commits have an issue opening and reading *names.txt* inside the SquareFactory class when running *server.py*. This is an error on my part due to my workspace hierarchy, and it will prevent the server from running unless you setup your file architecture like mine. However, the better fix is to simply alter the code (if for some reason you want to run the oldest working version). The fix:

    **Original *square.py*, line 27**
    ```python
    with open("python\\testing\\socket_squares\\names.txt", "r") as f:
    ```

    **Corrected *square.py*, line 27**
    ```python
    with open("names.txt", "r") as f:
    ```

## Contributing

This is a project for me to learn. While I'm not entirely against pull requests, I don't want everything completed and fixed for me. Minor changes are acceptable,
but opening an issue is likely a better way for something to get fixed. Thanks!

## Authors and acknowledgment

Kirigaine - Developer

A quick thanks to [maker2413](https://github.com/maker2413) for teaching me about requirements.txt and .python-version.

## License

[MIT](https://choosealicense.com/licenses/mit/)

## Project Status

This project is still ongoing.
