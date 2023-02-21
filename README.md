# Online Store developed in Python

## Index
1. Introduction
2. Developed in 
3. Try the app

## 1. Introduction 
This is an application that simulates a grocery store shopping cart.

## 2. Developed in
This app is developed in Python using:
* **Threads:** to start the two servers of the app (One processes the purchases and the other sends the images of the products to the client).
* **Non-blocking Sockets:** for client-server communication through TCP.
* **PyQt5:** for create the GUI  
* **Object-oriented programming** 

## 3. Try the app 
In order to run and deploy the project, you need to install:
* [Python 3.8 64bit](https://www.python.org/downloads/)
* PyQt5 `pip install pyqt5` in the console.

Once everything is installed, you download this repository and run the servidor_hilos.py file to start the servers `python servidor_hilos.py`

And finally, you run the cliente_interfaz.py file to connect to the server and make your purchases `python cliente_interfaz.py`
