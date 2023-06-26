"""

API Auto Test Python №4:

Авторизація на сайті завдяки API + Оновлення інформації Товару + Тестування

"""

import coreapi
import pytest_check as check

class TestUpdateItem:
    def test_updateitem(self):
        usersnames = "alextest24"
        passwords = "123456qwerty123!"

        # Initialize a client & load the schema document
        auth = coreapi.auth.BasicAuthentication(username=usersnames, password=passwords)
        client = coreapi.Client(auth=auth)
        schema = client.get("http://testsite.light-it.io/docs/")

        order_id = 212
        name = "Test_Product_220"
        owner = 63
        quantity = 10
        cost = 1005
        status = 1
        bid_type = 1

        # Interact with the API endpoint
        action = ["orders", "orders", "update"]
        params = {
            "id": order_id,
            "name": name,
            "owner": owner,
            "quantity": quantity,
            "cost": cost,
            "status": status,
            "bid_type": bid_type,
        }

        try:
            # Perform the API request
            result = client.action(schema, action, params=params)

            # JSON response output
            result = dict(result)
            print(f"Order Creation Done! JSON response:\n{result}")
            check.equal(result['name'], params["name"])
        except Exception as e:
            print(f"Order creation Error! Error msg: {str(e)}")
            check.equal({str(e)}, "Error!")