"""

API Auto Test Python №3:

Авторизація на сайті завдяки API + Створення Товару + Тестування

"""

import coreapi
import pytest_check as check

class TestCreateItem:
    def test_createitem(self):
        usersnames = "alextest24"
        passwords = "123456qwerty123!"

        # Initialize a client & load the schema document
        auth = coreapi.auth.BasicAuthentication(username=usersnames, password=passwords)
        client = coreapi.Client(auth=auth)
        schema = client.get("http://testsite.light-it.io/docs/")

        name = "Test_Product_220"
        owner = 63
        quantity = 10
        cost = 100
        status = 1
        bid_type = 1

        # Interact with the API endpoint
        action = ["orders", "orders", "create"]
        params = {
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
            print(f"Creation successful! JSON Response: \n{result}")
            check.equal(result['name'], params["name"])
        except Exception as e:
            print(f"Creation Error. Error msg: {str(e)}")
            check.equal({str(e)}, "Error!")