# K-trainee assignment
This is a K-trainee assignment. The purpose of this assignment was to make a microservice of any kind.

The backend of this assignment is programmed in Python3 programming language and Flask framework.

I have made a really simple hardware store backend that has three endpoints. One is to see what kind of products the store has. The second one is to show what is in your shopping cart. The third endpoint is for post methods to add products in the shopping cart. 

## How to install Python3 and Flask?
In order to run this program you need to install Python3 and Flask on your machine. 

To install Python3 on Ubuntu type in terminal: 

>sudo apt-get install python3.8 python3-pip

After installing python, install Flask. Run in Ubuntu terminal the following line:

>pip3 install Flask

### How to run this program?
To run this program, open terminal and navigate to the directory where you have set the program folder. In the program folder you will find app.py file. To start the server type in the terminal 

>flask run

now your backend should start running at [localhost:5000](localhost:5000).

The program can be found on Heroku at [https://k-trainee.herokuapp.com/api/products](https://k-trainee.herokuapp.com/api/products)

If you have postman installed on your machine you can test this program by making a post (by using POST method) to ```/api/shoppingcart```. Before you do this you can check that the cart is empty by making GET method to ```/api/shoppingcart```.

 You can find the list of available products at ```/api/products```. 
 
 You can also use cURL to POST or GET data.
 
 By typing the following command in terminal: 
 >curl -i --cookie cookie.txt --cookie-jar cookie.txt http://127.0.0.1:5000/api/shoppingcart 
 you can GET shopping cart data. 
 
 To POST type: 
 >curl -i --cookie cookie.txt --cookie-jar cookie.txt  -X POST http://127.0.0.1:5000/api/shoppingcart -H 'Content-Type: application/json' -d '{"id":456,"count":12}' 
 
 and to get the list of products:
>curl -i --cookie cookie.txt --cookie-jar cookie.txt http://127.0.0.1:5000/api/products
