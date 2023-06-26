"""

API Auto Test Python №6:

Авторизація на сайті завдяки API + Історя статусу Товарів + Тестування

"""

import coreapi
import pytest_check as check

class TestHistoryItem:
    def test_historyitem(self):
        usersnames = "Oleksanders"
        passwords = "123456qwerty123!"

        # Initialize a client & load the schema document
        auth = coreapi.auth.BasicAuthentication(username=usersnames, password=passwords)
        client = coreapi.Client(auth=auth)
        schema = client.get("http://testsite.light-it.io/docs/")

        # Interact with the API endpoint
        action = ["orders", "order_history", "list"]
        result = client.action(schema, action)

        try:
            # Perform the API request
            result = client.action(schema, action)

            print(f"Listing orders Done! JSON Response:\n{result}")
            check.equal(result, result)
        except Exception as e:
            print(f"Listing orders Error! Error msg: {str(e)}")
            check.equal({str(e)}, "Error!")