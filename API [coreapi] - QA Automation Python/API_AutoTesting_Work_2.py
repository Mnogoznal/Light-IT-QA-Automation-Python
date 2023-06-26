"""

API Auto Test Python №2:

Авторизація на сайті завдяки API + Тестування

"""

import coreapi
import pytest_check as check

class TestLogin:
    def test_login(self):
        # Initialize a client & load the schema document
        client = coreapi.Client()
        schema = client.get("http://testsite.light-it.io/docs/")

        username = "alextest24"
        email = "alextest25@mail.com"
        password = "123456qwerty123!"

        # Interact with the API endpoint
        action = ["profiles", "login", "create"]
        params = {
            "username": username,
            "email": email,
            "password": password,
        }

        try:
            # Perform the API request
            result = client.action(schema, action, params=params)

            # JSON response output
            result = dict(result)
            result['user'] = dict(result['user'])
            print(f"Login successful! JSON response:\n{result}")
            check.equal(result['user']['username'], params["username"])
        except Exception as e:
            print(f"Login Error! Error message: {str(e)}")
            check.equal({str(e)}, "Error!")