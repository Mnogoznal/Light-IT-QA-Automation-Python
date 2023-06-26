"""

API Auto Test Python №5:

Авторизація на сайті завдяки API + Видалення Товару + Тестування

"""

import coreapi
import pytest_check as check

class TestDeleteItem:
    def test_deleteitem(self):
        usersnames = "alextest24"
        passwords = "123456qwerty123!"

        # Initialize a client & load the schema document
        auth = coreapi.auth.BasicAuthentication(username=usersnames, password=passwords)
        client = coreapi.Client(auth=auth)
        schema = client.get("http://testsite.light-it.io/docs/")

        order_id = 212

        # Interact with the API endpoint
        action = ["orders", "orders", "delete"]
        params = {
            "id": order_id,
        }

        try:
            # Perform the API request
            result = client.action(schema, action, params=params)

            # JSON response output
            result = dict(result)
            print(f"Order del Done! JSON response:\n{result}")
            check.equal(result, params["id"])
        except Exception as e:
            print(f"Order del Error! Error msg: {str(e)}")
            check.equal({str(e)}, "Error!")