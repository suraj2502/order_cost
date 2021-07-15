# order_cost
To run this project
a) steps to run the code and get swagger

1-create a virtiual environment and activate it

    python3 -m venv api_env && source api_env/bin/activate
    
2-install requirements by below command

    pip3 install -r requirements.txt

3-start the server by running main.py file

    python3 main.py

go to http://0.0.0.0:8081/docs  to view the swagger 

use below api-endpoint url to get total cost of order by providing data in request body -->{ "order_items": [ { "name": "bread", "quantity": 2, "price": 2200 }, { "name": "butter", "quantity": 1, "price": 5900 } ], "distance": 1200, "offer": { "offer_type": "FLAT", "offer_value": 1000 } }

 test url --> http://0.0.0.0:8081/order_items/get_items_cost

b) Description


