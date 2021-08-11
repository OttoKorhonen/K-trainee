# K-trainee assignment
This is a K-trainee assignment. The purpose of this assignment was to make a microservice of any kind. The backend of this assignment is programmed in Python3 programming language and Flask framework. I have made a really simple hardware store backend that has three endpoints. One is to see what kind of products the store has. The second one is to show what is in your shopping cart. The third endpoint is for post methods to add products in the shopping cart. 

## How to install Python3 and Flask?
In order to run this program you need to install Python3 and Flask on your machine. To install Python3 on Ubuntu type in terminal sudo apt-get update and then sudo apt-get install python3.8 python3-pip. After installing python, install Flask. Run in Ubuntu terminal the following line pip3 install Flask.

### How to run this program?
To run this program, open terminal and navigate to the directory where you have set the program folder. In the program folder navigate to server folder where you will find app.py file. To start the server type in the terminal python3 app.py, now your backend should be running.

If you have postman installed on your machine you can test this program by making a post (by using post method) to localhost:5001/api/shoppingcart. Before you do this you can check that the cart is empty by opening your browser and by entering url localhost:5001/shoppingcart.

There is also a really simple React frontend programmed for this assignment. The program can be found in the same root folder in frontend folder. React installation instructions can be found online, so I won't be putting them here. To run the React program go to ~/frontend/src folder and type in terminal npm start. The program should start in your web browser. To add products in the cart just press the shopping cart icon. You can check your shopping cart again by going to localhost:5001/shoppingcart. You may have to refresh the page to see the added items.