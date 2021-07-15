# order_cost
To run this project
a) steps to run the code and get swagger

1-create a virtiual environment and activate it by running below command

    python3 -m venv api_env && source api_env/bin/activate
    
2-install requirements by below command

    pip3 install -r requirements.txt

3-start the server by running main.py file

    python3 main.py

go to http://0.0.0.0:8081/docs  to view the swagger 

use below api-endpoint url to get total cost of order by providing data in request body -->{ "order_items": [ { "name": "bread", "quantity": 2, "price": 2200 }, { "name": "butter", "quantity": 1, "price": 5900 } ], "distance": 1200, "offer": { "offer_type": "FLAT", "offer_value": 1000 } }

 test url --> http://0.0.0.0:8081/order_items/get_items_cost

b) Description

Fast-api is used as a backend framework to build this api end point ,which is the fastest framework of python and provides very good asynchronous support 

constraints:

quantity for any item should be less than 200 and greater than 0

Distance should be given in meters and should be less than 500000 m.

Offer type can only take two values- ("FLAT", "DELIVERY") and it is optional, declared offer_type schema as a enum. 

Length of the name of an Item should be maximum 300 characters and minimum 1 character

price has maximum value 500000 
