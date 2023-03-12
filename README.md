# Online Store developed in Python

## Index
1. [Introduction](https://github.com/IreneLopezM/Online-store-developed-in-Python#1-introduction)
2. [Developed in](https://github.com/IreneLopezM/Online-store-developed-in-Python#2-developed-in)
3. [Try the app](https://github.com/IreneLopezM/Online-store-developed-in-Python#3-try-the-app)

## 1. Introduction 
This is an application that simulates a grocery store shopping cart.

![App](https://user-images.githubusercontent.com/107958147/220238242-913c9bb8-dd8a-45db-a060-ab0d2ae3258e.JPG)

You can choose the products and add them to the shopping cart.

![Confirm](https://user-images.githubusercontent.com/107958147/220238571-ee5eda84-36ee-4f85-a50c-e8cbeeacf40b.JPG)

Also, you can see what is in your shopping cart.

![cart](https://user-images.githubusercontent.com/107958147/220238804-f1549355-d512-479d-a581-2fcd46bc7d5e.JPG)

And finally, make the purchase.

![purchase](https://user-images.githubusercontent.com/107958147/220239071-6ef16fb4-924d-4dbe-bc1b-d8f3e325a8d7.JPG)

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
